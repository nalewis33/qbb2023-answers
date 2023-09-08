#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt

"""
In the space below, create a function that implements the Wright-Fisher model. Your function should accept two arguments:

a starting allele frequency
the population size
Your function should run until one of the two alleles reaches fixation (i.e., your allele frequency hits 0 or 1).

In each generation, your function should take the current allele frequency and generate the allele frequency of the next generation by sampling from the binomial distribution.

Your function should return a list containing the allele frequencies at every generation, including the first and last generations.

Run your function with any starting allele frequency and a population of at least 100. Print the number of generations it takes to reach fixation.

Using that same data, create a plot of allele frequency over time throughout your simulation. I.e. the X axis is the generation, the Y axis is the frequency of your allele at that generation.
"""
#Psuedo code:
# Define a starting allele frequency
# Define a population size
# Input parameters for function


#Make a list to store our allele frequencies


# while our allele frequency is between 0 and 1:
# 	get new allele frequency for next generation
#	by drawing from the binomial distribution
#	(convert # of successes into a frequency)
#	Store allele frequency in allele frequency list



# Return a list of allele frequence at each time point
# Number of generations to fixation = length of list

def wright_fischer(n,p): #defining the function with input parameters n (population num), and p (allele starting frequency):
	p_list = [p] #defining list containing that will contain allele frequencies.
	while 0 < p < 1: #while the allele is not fixated (between a value of 0 and 1):
		wf = np.random.binomial(2*n, p) #running binomial distribution using n and p (doing 2*n due to there being 2 alleles)
		p = wf/(2*n) #calculating allele frequency by dividing wf by the number of chromosomes
		p_list.append(p) #adding 
	return(p_list) #return the list of frequencies from the function

"""
frequencies = wright_fischer(1000, 0.5) #test case using 10000 individuals and a starting frequency of 0.5
#print(frequencies) #printing to check
gen_frequency = len(frequencies)
print("The number of generations to fixation is", gen_frequency)
fig1, ax1 = plt.subplots()

ax1.plot(frequencies) #plotting the allelge 
ax1.set_ylabel("Allelic frequencies") #setting label for y axis (allelic frequencies)
ax1.set_xlabel("Number of generations") #setting label x axis (number of generation)
ax1.set_title("Time to Allele Fixation") #Adding title
fig1.savefig( "Exercise 1 Allele Frequency Plot" ) #saving figure as a png file
plt.close(fig1)
"""
"""
Exercise 2:
Because sampling from the binomial distribution is random, the behavior of this model changes every time that we run it. (To view this, run np.random.binomial(n, p) a few times on your own and see how the numbers vary). Run your model repeatedly (at least 30 iterations) and visualize all your allele frequency trajectories together on one plot. Remember that you can lines to a matplotlib figure using a for loop.

Run your model at least 1000 times and create a histogram of the times to fixation. If you want to see the distribution of times to fixation, this is an effective way of doing so.


"""

#Psuedo code:
# run function 30 times 
# visualize frequencies together on a histogram

fig2, ax2 = plt.subplots()
ax2.set_ylabel("Allelic frequencies") #setting label for y axis (allelic frequencies)
ax2.set_xlabel("Number of generations") #setting label x axis (number of generation)
ax2.set_title("Time to Allele Fixation") #Adding title

for i in range(30): #for 30 different runs of wright_fischer in a population
	frequencies = wright_fischer(100, 0.5) #giving an example
	ax2.plot(frequencies) #plotting all the frequencies. 

fig2.savefig( "Exercise_2_Allele_Frequency_Plot_30_Iterations" ) #saving figure as a png file

plt.close(fig2) #closing


#generate a histogram for time to fixation (number of generations)
gen_list = [] #creating empty list to store the values for number of generations for fixation
for i in range(1000): #for 1000 simulations:
	freq = wright_fischer(100,0.5) #generate the frequency using wright_fischer function/
	gen_fix = len(freq) #number of generations to fixation = length of frequency list
	gen_list.append(gen_fix) #add gen_fix integers to gen_list to generate list of generations to fixation
#print(gen_list) #printing gen_list to make sure a list of generation times is produced
#print(len(gen_list)) #checking length

fig3, ax3 = plt.subplots() #generation histogram
ax3.set_xlabel('Generations') #setting x label to generations
ax3.set_title('Number of Generations to Fixation') #Generating title
ax3.hist(gen_list) #Generating histogram from the generation list
fig3.savefig( "Exercise_2_Histogram" ) #saving figure as a png file
plt.close(fig3) #closing





