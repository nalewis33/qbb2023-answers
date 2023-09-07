#!/usr/bin/env python
import sys #setting up sys
import mean #importing my_mean function previously generated

fname = sys.argv[1] #using sys.argv.
integer_data = open(fname).readlines() #opening the integer_data file 

clean_int_list = [] #generating empty list to store 

for line in integer_data: #setting up for loop to generate the list of integers
	cleanline = line.rstrip("\n") #stripping the new line text from data
	cleanline = int(cleanline) #converting each input from str to int
	clean_int_list.append(cleanline) #adding each int value into the list

mean_from_file = mean.my_mean(clean_int_list) #using the my_mean() funciton, calculate the mean from the integer list
print(mean_from_file) #printing the average calculated by my_mean()

