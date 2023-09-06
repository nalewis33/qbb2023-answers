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


#Female Data:
# Find columns with female only samples
cols = [] #generating empty dataset for columns of interest
for i in range(len(samples)):
    if "female" in samples[i]:#finding samples that are for females (have "female" in the sample id)
        cols.append(i) #adding female columns into the empty column dataset

# Subset data of interest
expression = data[row, cols] #generating an expression set for the subset of females expressing at the value of that specific transcript

# Prepare data
x = samples[cols]
y = expression

# Plot data
fig1, ax1 = plt.subplots()

ax1.plot(x, y)
ax1.set_title( "sisA(FBtr0073461)" )
ax1.set_ylabel("mRNA abundance (RPKM)")
ax1.set_xlabel("Developmental Stage")
plt.xticks(rotation=90) #rotating x-axis label by 90 degrees
fig1.savefig( "FBtr0073461.png" )
plt.close( fig1 )

