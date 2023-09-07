#!/usr/bin/env python
import sys #setting up sys
import numpy as np

def diff_inflammation(a, b, c="Filename.csv"): #defining mean_inflammation function, pulling in a (patient index) and b(filename)
	fname=open(c, "r") #opening file
	patient_rows= fname.readlines() #reading each patient row
	patients= [] #generating empty patients list
	for i in patient_rows:
		i = i.rstrip() #stripping \n at the end of each row
		i = i.split(',') #splitting each row into individual lists
		patients.append(i) #appending to empty data set
	patient_interest1 = patients[a] #defining 1st patient of interest list based on whatever index was specified in function
	patient_interest2 = patients[b] #defining 2nd patient of interest list based on index specified
	patient_integers1= [] #empty dataset for the integer version of the first patient list
	for i in patients[a]:
		i = int(i)
		patient_integers1.append(i) #appending to the integer version of the list
	patient_integers2= [] #empty dataset for the integer version of the second patient
	for i in patients[b]:
		i = int(i)
		patient_integers2.append(i) #appending to the integer version of the list
	
	patient_diff = [] #Generating a list to store the differences between patient 1 and 2
	for i in range(len(patient_integers2)): #for each value spanning the length of the dataset (in order to hit all elements):
		diff = patient_integers1[i]-patient_integers2[i] #calculate the difference between each day of patient 2 and patient 1
		patient_diff.append(diff) #add each difference value into the diff list
	print(patient_diff) #print the list containing the difference each day between patient 1 and 2.

	fname.close() #closing file
	return(patient_diff) #returning the list of differences.


#Testing code to make sure it works	
diff_inflam = diff_inflammation(3, 2,  "inflammation-01.csv") #success!