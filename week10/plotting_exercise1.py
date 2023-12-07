#!/usr/bin/env python


import numpy as np
import pandas as pd
from pydeseq2 import preprocessing
from matplotlib import pyplot as plt

# read in data
counts_df = pd.read_csv("gtex_whole_blood_counts_formatted.txt", index_col = 0)

# read in metadata
metadata = pd.read_csv("gtex_metadata.txt", index_col = 0)

# normalize
counts_df_normed = preprocessing.deseq2_norm(counts_df)[0]

# log
counts_df_logged = np.log2(counts_df_normed + 1)

# merge with metadata
full_design_df = pd.concat([counts_df_logged, metadata], axis=1)

print(full_design_df)

#print(full_design_df.loc['GTEX-113JC', :])

GTEX_113JC_sig = counts_df_logged.loc['GTEX-113JC'][ counts_df_logged.loc['GTEX-113JC']>0] #selecting genes with nonzero expression
#print(GTEX_113JC_sig)

fig, ax = plt.subplots() #histogram generations
ax.hist(GTEX_113JC_sig, bins = 30, color = 'slategray') #I like colors
ax.set_xlabel('GTEX-113JC Expression (Log Normalized Counts)')
ax.set_ylabel('Frequency')
ax.set_title('GTEX-113JC Expresson Across Genes')
fig.savefig('GTEX-113JC.png')

#Exercise 1.2 
# For the gene MXD4, plot the distribution of expression (logged normalized counts) in males versus females. Upload this figure for the assignment.

male_MXD4 = full_design_df.loc[full_design_df['SEX']== 1, 'MXD4'] #pulling out male (sex = 1) MXD4 values from dataframe
female_MXD4 = full_design_df.loc[full_design_df['SEX'] == 2, 'MXD4'] #pulling out female (sex = 2) MXD4 values from dataframe

fig2, ax2 = plt.subplots()
ax2.hist(male_MXD4, bins = 30, alpha = 0.5, color = 'dodgerblue', label = 'Male')
ax2.hist(female_MXD4, bins = 30, alpha = 0.5, color = 'orchid', label = 'Female')
ax2.set_xlabel('MXD4 Expression (Log Normalized Counts)')
ax2.set_ylabel('Frequency')
ax2.legend()
ax2.set_title('MDX4 Expression Differences Between Sexes')
fig2.savefig('MDX4_Expression.png')

#Exercise 1.3
#Plot the number of subjects in each age category. Upload this figure for the assignment.

age_dist = full_design_df.AGE.value_counts() #pulling out the count for each age group
#print(age_dist)
age_dist = age_dist.reindex(['20-29', '30-39', '40-49', '50-59', '60-69', '70-79'])


fig3, ax3 = plt.subplots() #generating bar plot
ax3.bar(x = age_dist.index, height = age_dist, color = 'mediumorchid') #x is the age distribution ranges (given by index of value_counts()), height is the counts
ax3.set_xlabel('Age Ranges')
ax3.set_ylabel('Number of Subjects')
ax3.set_title('Number of Subjects in Each Age Range')
fig3.savefig('Age_Distribution.png')


#Exercise 1.4
#For the gene LPXN, plot the median expression (logged normalized counts) over time (i.e. in each age category), stratified by sex. Upload this figure for the assignment.

male_LPXN = full_design_df.loc[full_design_df['SEX']== 1, 'LPXN'] #pulling out male (sex = 1) LPXN values from dataframe
male_age = full_design_df.loc[full_design_df['SEX']== 1, 'AGE'] #pulling out male ages
male_LPXN = pd.concat([male_LPXN, male_age], axis = 1)

female_LPXN = full_design_df.loc[full_design_df['SEX'] == 2, 'LPXN'] #pulling out female (sex = 2) LPXN values from dataframe
female_age = full_design_df.loc[full_design_df['SEX'] == 2, 'AGE'] #pulling out female (sex = 2) age values from dataframe
female_LPXN = pd.concat([female_LPXN, female_age], axis = 1)

#Age ranges: 20-29, 30-39, 40-49, 50-59, 60-69, 70-79 (same in M and F)
m_20 = male_LPXN.loc[male_LPXN['AGE'] == '20-29', 'LPXN'] #pulling out each age group in males
#print(m_20)
m_30 = male_LPXN.loc[male_LPXN['AGE'] == '30-39', 'LPXN']
m_40 = male_LPXN.loc[male_LPXN['AGE'] == '40-49', 'LPXN']
m_50 = male_LPXN.loc[male_LPXN['AGE'] == '50-59', 'LPXN']
m_60 = male_LPXN.loc[male_LPXN['AGE'] == '60-69', 'LPXN']
m_70 = male_LPXN.loc[male_LPXN['AGE'] == '70-79', 'LPXN']
m_sum = [m_20, m_30, m_40, m_50, m_60, m_70]
m_avg = []
for age in m_sum:
	age_avg = age.median() #calculating average expression of each age group
	m_avg.append(age_avg) #adding into average data set
 
#print(m_avg)

f_20 = female_LPXN.loc[female_LPXN['AGE'] == '20-29', 'LPXN'] #pulling out each age group in females
#print(f_20)
f_30 = female_LPXN.loc[female_LPXN['AGE'] == '30-39', 'LPXN']
f_40 = female_LPXN.loc[female_LPXN['AGE'] == '40-49', 'LPXN']
f_50 = female_LPXN.loc[female_LPXN['AGE'] == '50-59', 'LPXN']
f_60 = female_LPXN.loc[female_LPXN['AGE'] == '60-69', 'LPXN']
f_70 = female_LPXN.loc[female_LPXN['AGE'] == '70-79', 'LPXN']
f_sum = [f_20, f_30, f_40, f_50, f_60, f_70]
f_avg = []
for age in f_sum:
	age_avg = age.median() #calculating average expression of each age group
	f_avg.append(age_avg) #adding into average data set
 

labels = ['20-29', '30-39', '40-49', '50-59', '60-69', '70-79'] #labels for x axis

#print(f_avg)

fig4, ax4 = plt.subplots() #setting up plot
ax4.scatter(x = labels, y = m_avg, alpha = 0.5, color = 'dodgerblue', label = 'Male') #male data- keeping the colors consistent between 1.4 and 1.1, woah
ax4.scatter(x = labels, y = f_avg, alpha = 0.5, color = 'orchid', label = 'Female') #female data- keeping the colors consistent between 1.4 and 1.1, woah
ax4.set_xlabel('Age Ranges')
ax4.set_ylabel('Median LPXN Expression')
ax4.legend()
ax4.set_title('Median LPXN Expression Over Time')
fig4.savefig('LPXN_Expression_Age.png') #saving figure as png