# A palindromic number reads the same both ways. The largest palindrome made from the product of 
# two 2-digit numbers is 9009 = 91 x99.
# Find the largest palindrome made from the product of two 3-digit numbers.

# Python Implementation

# function
#Time module for execution time calculation
import time

#Time at the start of program
start = time.time()

#Largest palindrome for example problem
largest_palindrome1 = 0

#For loop to check each and every multiplication
for i in range(100,1,-1):
	for j in range(100,1,-1):
		if i*j > largest_palindrome1:
			if str(i*j)[::-1] == str(i*j):
				largest_palindrome1 = i*j
				break
			else:
				continue
		break

#Printing of largest palindrome number
print(largest_palindrome1)

#Largest Palindrome for question
largest_palindrome2 = 0

#for loop to check every multiple
for i in range(1000,100,-1):
	for j in range(1000,100,-1):
		if i*j > largest_palindrome2:
			if str(i*j)[::-1] == str(i*j):
				largest_palindrome2 = i*j
				break
			else:
				continue
		break

#Printing the largest Palindrome number
print(largest_palindrome2)

#Time at the end of program
end_time = time.time()

#Printing the time taken
print(end_time - start)