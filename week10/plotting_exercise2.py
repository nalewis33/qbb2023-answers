#!/usr/bin/env python


import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

cats_uk_reference = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2023/2023-01-31/cats_uk_reference.csv') #reading in data

#print(cats_uk)
print(cats_uk_reference)

# Prey caught vs age of cats (separated by sex)- scatter 

m_cats = cats_uk_reference.loc[cats_uk_reference['animal_sex'] == 'm']#Separating out male cats
m_cats = m_cats.loc[m_cats['hunt'] == True] #removing cats that were not allowed to hunt
f_cats = cats_uk_reference.loc[cats_uk_reference['animal_sex'] == 'f'] #Separating out female cats
f_cats = f_cats.loc[f_cats['hunt'] == True] #removing cats that were not allowed to hunt
#print(m_cats)
#print(f_cats)

#m_age = m_cats.age_years.value_counts() #pulling out the counts for each age group
#print(m_age) #looking at ages for male cats

#pulling out data for male cats

m_0 = m_cats.loc[m_cats['age_years'] == 0.0, 'prey_p_month'] #pulling out age group, prey per month
#print(m_0)
m_1 = m_cats.loc[m_cats['age_years'] == 1.0, 'prey_p_month'] #pulling out age group, prey per month
m_2 = m_cats.loc[m_cats['age_years'] == 2.0, 'prey_p_month'] #pulling out age group, prey per month
m_3 = m_cats.loc[m_cats['age_years'] == 3.0, 'prey_p_month'] #pulling out age group, prey per month
m_4 = m_cats.loc[m_cats['age_years'] == 4.0, 'prey_p_month'] #pulling out age group, prey per month
m_5 = m_cats.loc[m_cats['age_years'] == 5.0, 'prey_p_month'] #pulling out age group, prey per month
m_6 = m_cats.loc[m_cats['age_years'] == 6.0, 'prey_p_month'] #pulling out age group, prey per month
m_7 = m_cats.loc[m_cats['age_years'] == 7.0, 'prey_p_month'] #pulling out age group, prey per month
m_8 = m_cats.loc[m_cats['age_years'] == 8.0, 'prey_p_month'] #pulling out age group, prey per month
m_9 = m_cats.loc[m_cats['age_years'] == 9.0, 'prey_p_month'] #pulling out age group, prey per month
m_10 = m_cats.loc[m_cats['age_years'] == 10.0, 'prey_p_month'] #pulling out age group, prey per month
m_11 = m_cats.loc[m_cats['age_years'] == 11.0, 'prey_p_month'] #pulling out age group, prey per month
m_12 = m_cats.loc[m_cats['age_years'] == 12.0, 'prey_p_month'] #pulling out age group, prey per month

male_ages = [m_0, m_1, m_2, m_3, m_4, m_5, m_6, m_7, m_8, m_9, m_10, m_11, m_12]
m_prey_avg = []
for age in male_ages:
	age_prey = age.median() #calculating average prey per month of each group
	m_prey_avg.append(age_prey) #adding into average data set
#print(m_prey_avg)

#Data for female cats: 
#f_age = f_cats.age_years.value_counts() #pulling out the counts for each age group
#print(f_age)
f_1 = f_cats.loc[f_cats['age_years'] == 1.0, 'prey_p_month'] #pulling out age group, prey per month
f_2 = f_cats.loc[f_cats['age_years'] == 2.0, 'prey_p_month'] #pulling out age group, prey per month
f_3 = f_cats.loc[f_cats['age_years'] == 3.0, 'prey_p_month'] #pulling out age group, prey per month
f_4 = f_cats.loc[f_cats['age_years'] == 4.0, 'prey_p_month'] #pulling out age group, prey per month
f_5 = f_cats.loc[f_cats['age_years'] == 5.0, 'prey_p_month'] #pulling out age group, prey per month
f_6 = f_cats.loc[f_cats['age_years'] == 6.0, 'prey_p_month'] #pulling out age group, prey per month
f_7 = f_cats.loc[f_cats['age_years'] == 7.0, 'prey_p_month'] #pulling out age group, prey per month
f_8 = f_cats.loc[f_cats['age_years'] == 8.0, 'prey_p_month'] #pulling out age group, prey per month
f_9 = f_cats.loc[f_cats['age_years'] == 9.0, 'prey_p_month'] #pulling out age group, prey per month
f_10 = f_cats.loc[f_cats['age_years'] == 10.0, 'prey_p_month'] #pulling out age group, prey per month
f_11 = f_cats.loc[f_cats['age_years'] == 11.0, 'prey_p_month'] #pulling out age group, prey per month
f_12 = f_cats.loc[f_cats['age_years'] == 12.0, 'prey_p_month'] #pulling out age group, prey per month
f_13 = f_cats.loc[f_cats['age_years'] == 13.0, 'prey_p_month'] #pulling out age group, prey per month



female_ages = [f_1, f_2, f_3, f_4, f_5, f_6, f_7, f_8, f_9, f_10, f_11, f_12, f_13]
f_prey_avg = []
for age in female_ages:
	age_prey = age.median() #calculating average prey per month of each group
	f_prey_avg.append(age_prey) #adding into average data set
#print(f_prey_avg)

m_labels = [ 0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0] #labels for x axis
f_labels = [ 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0]
#print(f_avg)

fig, ax = plt.subplots() #setting up plot
ax.scatter(x = m_labels, y = m_prey_avg, alpha = 0.5, color = 'dodgerblue', label = 'Male') #male data
ax.scatter(x = f_labels, y = f_prey_avg, alpha = 0.5, color = 'orchid', label = 'Female') #female data
ax.set_xlabel('Ages')
ax.set_ylabel('Average Prey per Month')
ax.legend()
ax.set_title('Average Prey Caught Amongst Age Group')
fig.savefig('Age_Prey.png') #saving figure as png

#Major takeaway: 2 year old cats are cold-blooded killers, apparently. 10 year old male cats are softies, which tracks because my cat is too lazy to hunt. 
print(cats_uk_reference.columns.values)

# Average number of hours indoor vs number of prey caught- histogram
indoors = cats_uk_reference['hrs_indoors']
prey = cats_uk_reference['prey_p_month']
#print(indoors)
#print(prey)

fig2, ax2 = plt.subplots()
ax2.scatter(x = indoors, y = prey, color= 'chartreuse') #scatter bar plot
ax2.set_xlabel('Hours Spent Indoors')
ax2.set_ylabel('Prey Caught per Month')
ax2.set_title('Cats who spend less time indoors catch more prey')
fig2.savefig('Indoors_vs_PPM.png')

# Average prey caught between cats who are fed wet food and those who are not: are the cats who are not spoiled with wet food worse hunters

wet_food = cats_uk_reference.loc[cats_uk_reference['food_wet'] == True]
only_wet = wet_food.loc[wet_food['food_dry'] == False, 'prey_p_month'] #pulling out those on only wet food (no dry)
wet_dry = wet_food.loc[wet_food['food_dry'] == True, 'prey_p_month'] #pulling out wet + dry food
wet_food_avg = only_wet.mean() #calculating mean prey per month
wet_dry_avg = wet_dry.mean() #calculating mean prey per month
wet_x = 'Wet Food Only' #adding labels for graph
wet_dry_x = 'Wet and Dry Food'
no_wet_food = cats_uk_reference.loc[cats_uk_reference['food_wet'] == False] #those without wet food (a sad life)
dry_only = no_wet_food.loc[no_wet_food['food_dry'] == True, 'prey_p_month']  #dry food only
no_wet_dry = no_wet_food.loc[no_wet_food['food_dry'] == False, 'prey_p_month'] #no dry or wet food
#print(no_wet_dry) #this set is empty, I will not include it
no_wet_food_avg = dry_only.mean() #calculating mean prey per month
no_wet_dry_avg = no_wet_dry.mean() #calculating mean prey per month
dry_x = 'No Wet Food' #adding labels for graph
none_x = "No Wet, No Dry Food"
fig3, ax3 = plt.subplots()
ax3.bar(x = wet_x, height = wet_food_avg, color = 'lightcoral') 
ax3.bar(x = wet_dry_x, height = wet_dry_avg, color = 'mediumturquoise')
ax3.bar(x = dry_x, height = no_wet_food_avg, color = 'mediumslateblue')
ax3.set_xlabel('Diet')
ax3.set_ylabel('Average prey caught per month')
ax3.set_title('Cats on a wet food only diet catch more prey per month')
fig3.savefig('Diet_Effect.png')
