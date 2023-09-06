#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

"""
Day 2 HW: Push code to Github after each point.

Exercise 1:
Starting with plot-sxl.py, create plot-sisA.py to visualize sisA (FBtr0073461) in a fashion similar to Lott et al 2011 PLoS Biology Fig 3A by adding elements in the following order. After each step, push your code and plot to your git repository and check your repository using the https://github.com web interface (i.e. results in four separate commits).

Plot female data
Add male data
Add 2*male data (HINT: 2 * np.array( y ))
Annotate plot (generalize x-axis to 10 not female_10, add title, add x- and y-axis labels)

Exercise 2:
Modify plot-sisA.py (do not create a new file) to load the transcripts information using open() and a for loop rather than np.loadtxt(). Remember that the first line is a header and should not be stored in the transcripts list. Push just your code to your git repository and confirm at https://github.com that your code no longer uses np.loadtxt().

Exercise 3:
Recover your original plot-sisA.py using git checkout <commit> plot-sisA.py. Push your code to your git repository and confirm at https://github.com that your code once again uses np.loadtxt().

Data from:
https://github.com/bxlab/cmdb-quantbio/raw/main/assignments/lab/bulk_RNA-seq/extra_data/all_annotated.csv
"""

#creating a data structure to store the title columns (transcript names, the first two columns)
transcripts = np.loadtxt( "all_annotated.csv", delimiter=",", usecols=0, dtype="<U30", skiprows=1 )
#print( "transcripts: ", transcripts[0:5] )

#Creating a data set to store the name of sampes (first row)
samples = np.loadtxt( "all_annotated.csv", delimiter=",", max_rows=1, dtype="<U30" )[2:]
#print( "samples: ", samples[0:5] )

#creating a data set with the actual numerical values we want to examine (removing the transcript and sample names)
data = np.loadtxt( "all_annotated.csv", delimiter=",", dtype=np.float32, skiprows=1, usecols=range(2, len(samples) + 2) )
#print( "data: ", data[0:5, 0:5] )

# Find row with data for transcript of interest sisA (FBtr0073461)
for i in range(len(transcripts)):
    if transcripts[i] == 'FBtr0073461':
        row = i


#Generating arrays for male and female:
# Find columns with gender-specific samples
cols_females = [] #generating empty dataset for columns of interest
cols_males = []
for i in range(len(samples)):
    if "female" in samples[i]:#finding samples that are for females (have "female" in the sample id)
        cols_females.append(i) #adding female columns into the empty column dataset
    else: #if not having females, assume they're male 
        cols_males.append(i)

# Subset data of interest
expression_female = data[row, cols_females] #generating an expression set for the subset of females expressing at the value of that specific transcript
expression_male = data[row, cols_males] #generating an expression set for subset of males expressing gene of interest

# Adding 2* male data (Exercise 1, part 3)
expression_male_2 = 2* np.array(expression_male) #doubling expression values for males and storing in a separate array


# Prepare data
x_female = samples[cols_females]
x_female = np.char.strip(x_female, 'female_') #stripping the 'female' text from the x-axis, so that the male and female developmental stages overlap
y_female = expression_female #setting up expression data for females
x_male = samples[cols_males]
x_male = np.char.strip(x_male, 'male_') #stripping the 'male_' text from the x-axis, so that male and female developmental stages can overlap.
y_male = expression_male  #setting up expression data for males
y_male_2 = expression_male_2 #Setting up expression data for 2*males

# Plotting data- males and females should be on the same x-axis
fig1, ax1 = plt.subplots() #setting up figure 1

ax1.plot(x_female, y_female, label = 'female') #plotting female expression data
ax1.plot(x_male, y_male, label = 'male') #plotting male expression data
ax1.plot(x_male,y_male_2, label = '2*male') #plotting 2* male expression data

ax1.legend() #adding in a legend
ax1.set_title( "sisA(FBtr0073461)" ) 
ax1.set_ylabel("mRNA abundance (RPKM)")
ax1.set_xlabel("Developmental Stage")
plt.xticks(rotation=90) #rotating x-axis label by 90 degrees

fig1.savefig( "FBtr0073461.png" ) #saving figure as a png file
plt.close( fig1 ) #closing figure

