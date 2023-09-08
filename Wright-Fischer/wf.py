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


"""
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

"""

#Exercise 3:
"""
We can use our model to investigate how changing the population size affects the time to fixation. Pick at least five population sizes greater than or equal to 50. For each population size, run the model at least 50 times and find the average time to fixation. Keep your allele frequency constant for all runs. Create a scatter or line plot of population size vs. average time to fixation.

We can do the same for allele frequencies. This time, pick a population size and vary the allele frequency. Run at least 10 trials for each allele frequency. If your this takes a while to run, decrease your population size. For me, 1000 individuals and 10 trials per allele frequency ran fast enough.
"""

# Run the frequency model for 5 different populations of size >50 
# For each population:
# 	Run at least 50 times
# 	Calculate average time to fixation across all 50 (sum of generations to fixation/ 50)
#Plot population size vs. average time to fixation
def avg_fixation_pop_50(n, p):
	gen_sim = [] #generating empty list to store values for length to fixation
	for i in range(50):
		freq = wright_fischer(n, p) #calculating frequency to fixation using previous wright_fischer function
		gen_fix = len(freq) #number of generations to fixation = length of frequency list
		gen_sim.append(gen_fix) #adding the generations to fixation value for each sim to a list
	#Now that gen_sim is defined, calculating the average:
	total_gens = 0 #setting up a variable to store the total per generation
	for i in gen_sim: #for each value in gen_sim (list of integers):
		total_gens += i #add the value to total_gens

	avg_fix_gen = total_gens/len(gen_sim) #calculate average fixation time as total generations times/length of the list of the list of simulation fixation points (50)
	return(avg_fix_gen) #return calculated average

	

pop_sizes = [500, 1000, 2000, 5000, 10000] #setting a list of different population sizes
avg_fix = [] #creating empty list for average fixation times
for i in pop_sizes: #for each index in pop_sizes:
	fix_time = avg_fixation_pop_50(i, 0.5) #calculating average fixation time
	avg_fix.append(fix_time) #appending average fixation time onto avg_fix list. 


# print(avg_fix) #printing to check
fig4, ax4 = plt.subplots() #generating graph
ax4.plot(pop_sizes, avg_fix)
ax4.set_title('Fixation time vs Population Size') #adding title
ax4.set_xlabel('Population Size') #adding x-axis label
ax4.set_ylabel('Fixation Time (# of Generations)') #adding y-axis label
fig4.savefig("Exercise_3_Population_Size") #saving figure
plt.close(fig4) #closing figure

#Run frequency model for 5 different populations of the same size, with 5 different allelic frequencies
# Run at least 10 times
# Calculate average time to fixation across simulations
# Plot allelic frequency vs average time to fixation


allele_set = [0.1, 0.25, 0.5, 0.75, 0.95] #setting a list of different allele frequencies
avg_fix2 = [] #creating empty list for average fixation times
for i in allele_set: #for each index in pop_sizes:
	fix_time2 = avg_fixation_pop_50(1000, i) #calculating average fixation time with 100 individuals and varying population size
	avg_fix2.append(fix_time2) #appending average fixation time onto avg_fix2 list. 


# print(avg_fix) #printing to check
fig5, ax5 = plt.subplots() #generating graph
ax5.plot(allele_set, avg_fix2)
ax5.set_title('Fixation time vs Allelic Frequencies') #adding Title
ax5.set_xlabel('Allelic Frequencies') #Labeling x-axis
ax5.set_ylabel('Fixation Time (# of Generations)') #labeling y-axis
fig5.savefig("Exercise_3_Allele_Frequencies") #saving figure
plt.close(fig5) #closing figure
