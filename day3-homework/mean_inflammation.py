#!/usr/bin/env python
import sys #setting up sys
import mean #importing my_mean function previously generated



def mean_inflammation(a, b="Filename.csv"): #defining mean_inflammation function, pulling in a (patient index) and b(filename)
	fname=open(b, "r") #opening file
	patient_rows= fname.readlines() #reading each patient row
	patients= [] #generating empty patients llist
	for i in patient_rows:
		i = i.rstrip() #stripping \n at the end of each row
		i = i.split(',') #splitting each row into individual lists
		patients.append(i) #appending to empty data set
	patient_interest = patients[a] #defining patient of interest list based on whatever index was specified in function
	#print(patient_int)
	patient_integers= [] #empty dataset for the integer version of the patient list
	for i in patients[a]:
		i = int(i)
		patient_integers.append(i) #appending to the integer version of the list
	
	patient_mean_inflammmation = mean.my_mean(patient_integers) #calling previously generated my_mean function to calculate the mean of the patient of interest.
	print(patient_mean_inflammmation) #printing mean inflammation value
	fname.close() #closing file
	return(patient_mean_inflammmation) #returning the calculated mean.


#test for mean inflammation
#mean_inflam = mean_inflammation(3, "inflammation-01.csv") #success!





