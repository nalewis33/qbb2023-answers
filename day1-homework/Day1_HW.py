#!/usr/bin/env python
import numpy #importing numpy to use for calculations, namely exercise 3
"""
Day 1 Homework: 
In this dataset, each row represents a different patient. Each column represents a different day. Each element in the dataset is the number of arthritis flare-ups that a patient has in a given day.

For each exercise, please submit your code along with your answer. You can have one script per exercise, or have all exercises together in one larger script – either way is fine. Since we haven’t yet learned how to write to a file in Python, it is ok to print out your answers and then manually copy them over to a text file.

"""

#Exercise 1: Print the number of flare-ups that the fifth patient had on the first, tenth, and last day.
f = open("inflammation-01.csv", "r") #opening the csv file as read only
print("Exercise 1: Printing first, tenth, and last flare-ups of patient 5") #printing start of exercise 1

rows = f.readlines() #each row is a patient- yields a list of each day
#print(type(rows))
#print(rows)

patients=[] #creating an empty list for patient values

for i in rows:
	i = i.rstrip() #stripping \n at the end of each row
	patient_list = i.split(",") #splitting each row (patient) into individual lists, separated by commas
	#patient_int= int(patient_list[0:-1])
	#for day in patient_list:
	#	day_int = int(day)
	#print(patient_list) #prints each patient iteratively (just checking to see if this works)
	patients.append(patient_list) #storing patient lists in the patients list set


#print(patients[4]) #checking to see if I can print the list for patient #5 (element 4)
patient5 = patients[4] #creating a separate list for patient 5, pulling from the total patient list (element 4 in the lsit)
#print(patient5) #looking at patient5 set
print(type(patient5[0])) #checking type
print(patient5[0], patient5[9], patient5[-1]) #printing patient 5's day one, day ten, and final day flare-ups
"""
Exercise 2: Caluclating Averages
For each patient, calculate the average number of flare-ups per day. Print the average values for the first 10 patients.

These are the row averages - for example, patient 1 has 5.45 flare-ups per day on average; patient 2 has 5.425 flare-ups per day on average.
"""

print("Exercise 2: First 10 average of flare-ups per patient") #print exercise 2 start

flare_avg = [] #creating a list to store the average # of flare-ups for each patient


for patient_ind in patients: #for loop for each individual patients
	total = 0 #creating a total variable to store sum of each patient
	for day in patient_ind: #for each day (value) in each patient's dataset
		day_int = int(day) #converting each day (value) to an integer (was previously a string, can't do math on that)
		total += day_int #generating a total for each patient, the sum of each day total (as an int)
	patient_avg = total/len(patient_ind) #to calculate average, divide by the total number of days using length of patient_ind
	flare_avg.append(patient_avg) #adding each patient average into a list that will carry all averages for all patients


print(flare_avg[0:10]) #printing the first 10 values (averages for first 10 patients, elements 0-9)

#Exercise 3: Finding Maximum and Minimum Values
#Using the average flare-ups per day calculated in part 2, print the highest and lowest average number of flare-ups per day.
print("Exercise 3: Max and Min average flare-ups") #print exercise 3 start

print(numpy.max(flare_avg)) #print the max values in the flare_avg dataset using numpy
print(numpy.min(flare_avg)) #print the min value in the flare_avg dataset using numpy

#Exercise 4: Differences Between Patients
#For each day, print the difference in number of flare-ups between patients 1 and 5.
print("Exercise 4: Difference in flare-ups between Patient 1 and Patient 5 each day") #print exercise 4 start

patient1 = patients[0] #creating a dataset of the values for patient one, derived from previously generated patients dataset (see Exercise 1)
#print(patient1)
patient1_int = [] #generating data set to hold integer values for patient 1 (currently string values)
for day in patient1: #for each day (value) in patient 1
	day_int = int(day) #converting each day value from string to int
	patient1_int.append(day_int) #adding day_int value into patient1_int list set
#print(patient1_int) #printing list to see 
#print(type(patient1_int[4])) #checking data types to make sure things are int type

patient5_int = [] #generating data set to hold integer values for patient 5 (currently string values)
for day in patient5: #for each day (value) in patient 5
	day_int = int(day) #converting each day value from string to int
	patient5_int.append(day_int) #adding day_int value into patient5_int list set
#print(patient5_int) printing list to see 
#print(type(patient5_int[4])) #checking data types to make sure things are int type


patient_diff = [] #Generating a list to store the differences between patient 1 and 5
for i in range(len(patient5_int)): #for each value spanning the length of the dataset (in order to hit all elements):
	diff = patient1_int[i]-patient5_int[i] #calculate the difference between each day of patient 5 and patient 1
	patient_diff.append(diff) #add each difference value into the diff list
print(patient_diff) #print the list containing the difference each day between patient 5 and 1.




f.close() #closing the inflammation file