#!/usr/bin/env python3
#Author: Maharnav Singhal

n = int(input("Enter the number of stars: "))
no = n
if(no%2 != 0):
	print("Sorry, wrong input. The number of stars should be even within a range of 8-20 (both included)")
	exit()
	
spaces, no, a, b = 0, n, -2, 1
for i in range(0, no):
	if(n == 0):
		n, spaces = 2, spaces-b
		a, b = 2, -1
	sp = spaces
	N = n

	for j in range(0,sp):
		print(" ", end="", sep="")
	for j in range(0, N):
		print("*", end="", sep="")
		
	print("\n")
	n = n + a
	spaces = spaces + b
	
	