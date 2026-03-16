# What does this piece of code do?
# Answer:This code generate 11 random integers between 1-10, sum them up and print the sum.

# Import libraries
# randint allows drawing a random number,
# e.g. randint(1,5) draws a number between 1 and 5
from random import randint

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
from math import ceil

total_rand = 0
#initialize total rand
progress=0
#initialize progress
while progress<=10:
	#when the number of thr loops not exceed 10, countinue the loop
	progress+=1
	#the number of loop+1
	n = randint(1,10)
	#generate a integer n from 1 to 10 randomly
	total_rand+=n
	#add the new n to the sum of previous n

print(total_rand)
#output the sum of "n"s

