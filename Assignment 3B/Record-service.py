#########################################################################
# Author : Maharnav Singhal                                             #
# Author Id : 2021115001                                                #
# Date : 05-2022                                                        #
# Program usecase: Analysis of company growth according to Given Data   #
#########################################################################

# Importing SqLite3 for database management
import sqlite3
import csv

# Emptying the Database file, and creating if not exists
with open("record.db", "w") as fp:
    pass

# Connecting with databse and making cursor instance with connection
mydb = sqlite3.connect("record.db")
cursor_obj = mydb.cursor()

# Creating Ticker table and Metrics table as per given format
cursor_obj.execute("""create table Ticker (
            "Date" datetime NOT NULL,
            "Company Name" TEXT,
            "Industry" TEXT,
            "Previous Day Price" TEXT DEFAULT 'NA',
            "Current Price"	TEXT,
            "Change in Price" TEXT DEFAULT 'NA',
            "Confidence" TEXT )"""
                   )

cursor_obj.execute("""create table Metrics (
            KPIs TEXT, Metrics TEXT )"""
                   )

# Reading the Controls File; this determines the flow of further processing
control_list = list()
with open("./Control/control.csv", 'r') as fp:
    csv_reader = csv.reader(fp)
    next(csv_reader)

    for row in csv_reader:
        control_list.append(row)

# Creating Dates & respective files array, makes the code flexible
dates = ["2022-05-20", "2022-05-21", "2022-05-22", "2022-05-23", "2022-05-24"]
files = ["2021115001-20-05-2022.csv", "2021115001-21-05-2022.csv",
         "2021115001-22-05-2022.csv", "2021115001-23-05-2022.csv",
         "2021115001-24-05-2022.csv"
         ]

# Storing the 1st day data with assumption of no previous data
with open("./Record/" + files[0], "r") as fp:
    csv_reader = csv.reader(fp)
    next(csv_reader)

    for row in csv_reader:
        cursor_obj.execute("""insert into Ticker(
                    "Date","Company Name","Industry","Current Price",
                    "Confidence") values("%s", "%s", "%s", "%s", "%s")
                    """ % (dates[0], row[0], row[1], str(row[2]),
                           control_list[-1][2]))


# Reading the remaining files and getting previous day data
# Computing changes and pushing data into Ticker table according to controls
for i in range(1, len(files)):
    with open("./Record/" + files[i], "r") as file:
        csv_reader = csv.reader(file)
        next(csv_reader)

        for row in csv_reader:
            # Getting data for the previous day
            cursor_obj.execute(
                """select "Current Price", "Company Name", Date from Ticker
                where "Company Name" = "%s" and "Date" = "%s"
                """ % (row[0], dates[i - 1])
            )
            result = cursor_obj.fetchone()
            if result is None:
                cursor_obj.execute("""insert into Ticker(
                    "Date","Company Name","Industry","Current Price",
                    "Confidence") values("%s", "%s", "%s", "%s", "%s")
                    """ % (dates[i], row[0], row[1], str(row[2]),
                           control_list[-1][2]))
                continue

            last_price = float(result[0])
            curr_price = float(row[2])
            percent_change = (curr_price - last_price) / last_price * 100
            confidence = "NA"

            # Opertaing on the data
            for control_line in control_list:
                if control_line[0] == row[1]:
                    if control_line[1][0] == '<':
                        percentage = float(control_line[1].strip()[1: - 1])
                        if percent_change < percentage:
                            confidence = "Low"
                            break
                    elif control_line[1][0:2] == '>=':
                        percent_list = control_line[1].split('&')
                        bottom = float(percent_list[0].strip()[2: - 1])
                        above = float(percent_list[1].strip()[2: - 1])
                        if bottom <= percent_change <= above:
                            confidence = "Medium"
                            break
                    elif control_line[1][0] == '>':
                        percentage = float(control_line[1].strip()[1: - 1])
                        if percent_change > percentage:
                            confidence = "High"
                            break

            cursor_obj.execute("""insert into Ticker values
            ("%s", "%s", "%s", "%s", "%s", "%s", "%s"
                )""" % (dates[i], row[0], row[1], str(last_price),
                        str(curr_price), str(percent_change), confidence))

# Set the Best Listed Industry in Metrics table according to max Highs
cursor_obj.execute("""select "Industry",
            sum(case when Confidence='High' Then 1 else 0 end) as count_HIGH
            from Ticker group by "Industry"
            order by count_HIGH desc"""
                   )
result = cursor_obj.fetchone()
cursor_obj.execute(
    "insert into Metrics values('Best Listed Industry', \"%s\");" % result[0])

# Set the Worst Listed Industry in Metrics table according to max Lows
cursor_obj.execute("""select "Industry",
            sum(case when Confidence='Low' Then 1 else 0 end) as count_LOW
            from Ticker group by "Industry"
            order by count_LOW desc"""
                   )
result = cursor_obj.fetchone()
cursor_obj.execute(
    "insert into Metrics values('Worst Listed Industry', \"%s\");" % result[0])

# Getting the relative order of companies based on the 3 given criterias
cursor_obj.execute("""select "Company Name","Change in Price" from Ticker
            where "Change in Price" != "NA"
            order by cast("Change in Price" as decimal) desc,
            (cast("Previous Day Price" as decimal) -
            cast("Current Price" as decimal)) desc,
            "Company Name" asc"""
                   )
result = cursor_obj.fetchall()

# Set the Best Company and it's percent Gain in Metrics table
cursor_obj.execute("insert into Metrics values('Best Company', \"%s\");" %
                   result[0][0])
cursor_obj.execute(
    "insert into Metrics values('Gain %%', \"%s\");" % result[0][1])

# Set the Worst Company and it's percent Gain in Metrics table
cursor_obj.execute("insert into Metrics values('Worst Company', \"%s\");" %
                   result[-1][0])
cursor_obj.execute(
    "insert into Metrics values('Loss %%', \"%s\");" % result[-1][1])

# Commiting all above changes
mydb.commit()
