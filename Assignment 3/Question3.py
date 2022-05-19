#!/usr/bin/env python3
#Author: Maharnav Singhal

string = []

for i in range (10):
	if(i == 0):
		temp = input("Enter 1st word: ")
		
	elif(i == 1):
		temp = input("Enter 2nd word: ")
		
	elif(i == 2):
		temp = input("Enter 3rd word: ")
		
	else:
		temp = input("Enter "+str(i+1)+"th word: ")
		
	string.append(temp)
	
order_check = int(input("Enter 0 for ascending or 1 for descending: "))

string.sort(reverse = bool(order_check))

for i in string:
	print(i)

temp = input("Enter additional word: ")
string.append(temp)

string.sort(reverse = bool(order_check))

for i in string:
	print(i)