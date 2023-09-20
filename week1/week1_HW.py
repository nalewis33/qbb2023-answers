#!/usr/bin/env python

import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import scipy.stats as sps
import statsmodels.formula.api as smf
import statsmodels.api as sm 


"""
Data are taken from Halldorsson, B. V., Palsson, G., Stefansson, O. A., Jonsson, H., Hardarson, M. T., Eggertsson, H. P., … & Gudjonsson, S. A. (2019). Characterizing mutagenic effects of recombination through a sequence-level genetic map. Science, 363(6425).

Read the abstract from the above paper to understand the context of the datasets you will be using. The data you need for this assignment has already been loaded onto your laptop. There are two files we’ll be using for this assignment:

information about the number and parental origin of each de novo mutation detected in an offspring individual (i.e. “proband”), stored in /Users/cmdb/cmdb-quantbio/assignments/bootcamp/statistical_modeling/extra_data/aau1043_dnm.csv
ages of the parents of each proband, stored in /Users/cmdb/cmdb-quantbio/assignments/bootcamp/statistical_modeling/extra_data/aau1043_parental_age.csv
You can use this data as is, or make copies of it in your submission directory for this assignment. If you do make copies in your submission directory, don’t forget to add them to your .gitignore file within the submission directory.

Before beginning the assignment, you should examine the two files (with less -S perhaps) to make sure you understand how they’re organized.

"""

"""


"""
#Exercise 1.1 : load the aa1043_dnm.csv dataset into a pandas data frame (note that data is already saved on this computer)

DNM = pd.read_csv("/Users/cmdb/cmdb-quantbio/assignments/bootcamp/statistical_modeling/extra_data/aau1043_dnm.csv") #loading in aa1043_dnm.csv dataset using pandas

#print(DNM) #examining the dataframe. 

#Exercise 1.2: You first want to count the number of paternally and maternally inherited DNMs in each proband. 
#Using this dataframe, create a dictionary where the keys are the proband IDs and the value associated with each key is a list of length 2,
# where the first element in the list is the number of maternally inherited DNMs and the second element in the list is the number of paternally inherited DNMs
# for that proband. 
#You can ignore DNMs without a specified parent of origin.

#Psuedo code: 
# for each unique proband_id value (the key): 
# make a list for the key containing:
# number of maternally inherited DNMS (Phase_combined = mother)
# number of paternally inherited DNMS (Phase_combined = father)
# ignore NaN values

deNovoCount = {} #creating empty dictionary to start adding things in to in the for loop.

for i in range(len(DNM)): #for every row in DNM: 
	proband_id = DNM.loc[i, "Proband_id"] #looping through dataset to get the proband_id for each row
	parent = DNM.loc[i, 'Phase_combined'] #grabbing the Phase-combined (parental inheritance) from each dictionary (mother or father), setting value to the parent variable
	if proband_id not in deNovoCount: #if the proband_id is not already in the dictionary:
			deNovoCount[proband_id] = [0,0] #create the key for each proband ID and setting a base list of [0, 0] (no maternal or paternal DNMs)- for each value that is maternal or paternal, we will add one to appropriate index
	if parent == 'mother': #if the parental inheritance is from the mother:
		deNovoCount[proband_id][0] += 1 #add 1 to the 0th element of the list
	elif parent == 'father': #if the parental inheritance is from the father:
		deNovoCount[proband_id][1] +=1 #add 1 to the 1st element of the list
#Note: ignoring any values whether maternal or paternal inheritance is not specified. 
#print(deNovoCount) #printing deNovoCount to check 

deNovoCountDF = pd.DataFrame.from_dict(deNovoCount, orient = 'index', columns = ['maternal_dnm', 'paternal_dnm']) # Exercise 1.3: converting dictionary into a table.

print(deNovoCountDF) #printing to look at
# Exercise 1.4

parent_age = pd.read_csv('/Users/cmdb/cmdb-quantbio/assignments/bootcamp/statistical_modeling/extra_data/aau1043_parental_age.csv', index_col = 'Proband_id') #reading in parent age dataset, setting index column to the proband ID
print(parent_age) #printing to look at

#Exercise 1.5
mergedDF = pd.concat([deNovoCountDF, parent_age], axis = 1, join = 'inner') #concatenating 

print(mergedDF) #looking at merged dataframe to confirm data is merged- success





