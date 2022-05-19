#!/usr/bin/env python3
#Author: Maharnav Singhal

import os

n = int(input("Enter no of students: "))
no = n

ranks = []
data = {}
for i in range (0,no):
	if(i == 0):
		roll = int(input("Enter the roll number for 1st student: "))
				
	elif(i == 1):
		roll = int(input("Enter the roll number for 2nd student: "))
				
	elif(i == 2):
		roll = int(input("Enter the roll number for 3rd student: "))
				
	else:
		roll = int(input("Enter the roll number for "+str(i+1)+"th student: "))		
		
	name = input("Enter the name: ")
	
	data[roll] = {}
	data[roll]['Name'] = name
	
	math = int(input("Enter the math marks: "))
	cse = int(input("Enter the CSE marks: "))
	sci = int(input("Enter the Science marks: "))
	
	data[roll]['Math'] = math
	data[roll]['Cse'] = cse
	data[roll]['Sci'] = sci
	data[roll]['Total'] = math+cse+sci
	data[roll]['Mean'] = data[roll]['Total']/3
	
	temp = [data[roll]['Math'],data[roll]['Cse'],data[roll]['Sci']]
	temp.sort()
	data[roll]['Median'] = temp[1]
	
	ranks.append(data[roll]['Total'])
		
#clearing the screen after taking input
if(os.name == 'posix'):
	os.system('clear')
else:
	os.system('cls')
	
ranks = list(set(ranks))
ranks.sort()

no = n
for roll in data:
	print(roll,": ",data[roll]['Name'])

print()
while(True):
	i = int(input("Enter the roll number of the student you want the data (or -1 to exit): "))
	
	print()
	if(i == -1):
		exit()
		
	if(i in data):
		print("Name: ",data[i]['Name'],"\n","Maths: ",data[i]['Math'],", CSE: ",data[i]['Cse'],", Science: ",data[i]['Sci'],"\n","Mean marks: ",data[i]['Mean'],", Median marks: ",data[i]['Median'],"\n","Rank: ",ranks.index(data[i]['Total'])+1, sep="")
		print()
	
	else:
		print("Sorry, no such roll number exists in the database. Please try again\n")