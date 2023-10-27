#!/usr/bin/env python

import matplotlib.pyplot as plt
import re #importing re to split the vcf file by multiple different separators.
import numpy as np

read_depths = [] #generating empty list to contain read depths, which in the VCF file are ID'd as DP. 
genotype_quality = [] #generating empty list for genotype quality values, which are ID = GQ
allele_freq = [] #empty data set for allele frequencies
moderate= [] #empty data set for variants with moderate effects
high = [] #empty data set for variants with high effects
low = [] #empty data set for variants with low effects
modifier = [] #empty data sets for variants with modifier effect

for line in open('ann_vcf.vcf'):
    if line.startswith('#'):
        continue
    fields = line.rstrip('\n')
    fields = re.split('\t|=|;|:', fields) #splitting by multiple characters using re.split. 
    # grab what you need from `fields`
    
    for i in range(len(fields)):
    	if fields[i] == "DP" and fields[i+1] == "AD": #if i = "DP" and the following value is NOT AD 
    		k = 1
    		while (i + 9*k) <= len(fields):
    			read_depths.append(fields[i+9*k])#add the next value in the list to the read_depths list-
    			k += 1	
    	elif fields[i] == "GQ":
    		j = 1
    		while (i + 9*j) <= len(fields): #until you exceed the length of fields (indicating no more GQ values)
    			genotype_quality.append(fields[(i + 9*j)]) #append in the value for genotype quality, which is 9 values up from GQ 
    			j += 1 #add 1. Note: expecting 10 values per fields, but in case there are more for whatever reason this code works
    	elif fields[i] == "AF":
    		allele_freq.append(fields[i+1])
    	elif "LOW" in fields[i]: #if location contains LOF, indicating loss of function mutation
    		low.append(fields[i]) #add to LOF dataset
    	elif "MODERATE" in fields[i]: #if location contains NMD, indicating nonsense-mediated decay mutation
    		moderate.append(fields[i]) #add to NMD dataset
    	elif "HIGH" in fields[i]:
    		high.append(fields[i])
    	elif "MODIFIER" in fields[i]:
    		modifier.append(fields[i])

#print(fields) #looking at separated fields
#print(read_depths) #looking at read depths- need to remove empty values and convert to integers. 

#removing missing reads from read_depths, which are denoted by '.'- will also convert values to ints 
read_depths_filtered = []

for i in range(len(read_depths)):
	if read_depths[i] != '.':
		read_depths_filtered.append(int(read_depths[i]))

#print(read_depths_filtered)
#print(len(read_depths_filtered))

#print(genotype_quality) #looking at genotype quality set- have empty reads that need to be removed. 
#Removing empty values from genotype quality, which are denoted as '.' in the data.

gq_filtered = [] #new empty data set for only actual values
for i in range(len(genotype_quality)):
	if genotype_quality[i] != '.': #if the value is an actual value
		gq_filtered.append(float(genotype_quality[i])) #add to gq_filtered

#print(gq_filtered) #looking at new gq set
#print(len(gq_filtered)) #looking to see reduction in length. 


#print(allele_freq) #printing to look at
#print(len(allele_freq)) #looking at length. 

#allele_freq has values that are two values separated by a comma- need to split them before converting everything to ints. 

allele_freq_float = [] #empty dataset for our final float values
for i in range(len(allele_freq)): 
	if ',' in allele_freq[i]: #if there is a comma in allele_freq (indicating double value)
		doubles = allele_freq[i]
		values = doubles.split(',') #split values by the comma
		i = 0
		while i < len(values): 
			allele_freq_float.append(float(values[i])) #add each value (as a float) to the float data set until all values are added.
			i += 1
	else:
		allele_freq_float.append(float(allele_freq[i])) #convering values to float and adding to dataset. 

#print(len(allele_freq_float)) #looking to see change in length
#print(allele_freq_float) #looking at dataset
#print(type(allele_freq_float[25]))

#Bar plot predicting effects of variants
muts = ['LOW', 'MODERATE', 'HIGH', 'MODIFIER'] #defining effects to look at
mut_counts = [len(low), len(moderate), len(high), len(modifier)] #length of each dataset containing all variants with corresponding effect
mut_colors = ['dodgerblue', 'orange', 'crimson', 'darkgreen'] #we're adding colors!
#print(mut_counts) #looking at counts for my own curiousity. 


fig1, ax  = plt.subplots(2, 2, figsize = (10,10)) #setting up subplots- will do a 2x2 grid
ax[0,0].hist(read_depths_filtered, range = (0, 50), bins = 30, color = 'mediumorchid') #histogram of read_depths- there are a few extreme outliers, so I am manually inputting a range of 0-50, where a majority of read depths lie. 
ax[0,0].set_ylabel('Number of Samples')
ax[0,0].set_xlabel('Read Depth')
ax[0,0].set_title('Read Depth Across Samples')
ax[0,1].hist(gq_filtered, bins = 30, color = 'steelblue') #histogram of genotyping quality- going for bright colors here
ax[0,1].set_ylabel('Number of Samples')
ax[0,1].set_xlabel('Genotype Quality')
ax[0,1].set_title('Genotype Quality Across Samples')
ax[1,0].hist(allele_freq_float, bins = 30, color = 'firebrick') #histogram for allele frequencies
ax[1,0].set_ylabel('Number of Samples')
ax[1,0].set_xlabel('Allele Frequencies')
ax[1,0].set_title('Allele Frequencies Across Samples')
ax[1,1].bar(muts, mut_counts, color = mut_colors)
ax[1,1].set_ylabel('Number of Variants')
ax[1,1].set_xlabel('Predicted Effect by VCF')
ax[1,1].set_title('Predicted Effects of Variants')
fig1.tight_layout() #tight layout to make things not overlap. 
fig1.savefig( "variant_analysis.png") #saving to a png file. 
plt.close(fig1)