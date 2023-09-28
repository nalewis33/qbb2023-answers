#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

#Exercise 1.2: simulate sequencing 3x coverage of a 1Mbp genome with 100bp reads. Note that you do not need to actually simulate the sequences of the reads, you can just randomly sample positions in the genome and record the coverage. You do not need to consider the strand of each read.


def simulate_coverage(coverage, genome_len, read_len, figname): #defining a function to generate these simulations, where variables specified include the coverage we want. the lengths of our genomes and reads, as well as a figure to save the simulation to.
	coverage_arr = np.zeros(genome_len) #generating an array that is the length of our genomes- right now, filling the array with 0s 
	num_reads = int(genome_len * coverage / read_len) #calculating the number of reads- not that we need to convert to an int (can't have a fraction of a read)
	#print(coverage_arr)
	low = 0
	high = genome_len - read_len # calculating the highest genome read you can do
	start_positions = np.random.randint(low= 0, high = high + 1, size = num_reads) #generating random number in the range of num_reads
	for start in start_positions: 
		coverage_arr[start: start + read_len] += 1 #adding into the bucket for each position 
	x = np.arange(0, max(coverage_arr)+1) 
	sim_0cov = genome_len - np.count_nonzero(coverage_arr) #calculating the number of bps that have no coverage (reads)
	sim_0cov_pct = 100 * sim_0cov/ genome_len #calculating the percentage of the genome that has no coverage (bp)
	print(f'in the simulation, there are {sim_0cov} bases with 0 coverage') #printing number of bps with no reads
	print(f'this is {sim_0cov_pct} % of the genome') #printing the percentage. 
	#Get Poisson distribution
	y_poisson = stats.poisson.pmf(x, mu = coverage) * genome_len #multiplying by genome length to get on the same scale as our histogram. 
	#print(y_poisson)

	#Get normal distribution: 
	y_normal = stats.norm.pdf(x, loc = coverage, scale = np.sqrt(coverage)) * genome_len
	#print(y_normal)

	fig, ax = plt.subplots() #generating histogram plot
	ax.hist(coverage_arr, bins = x, align = 'left', label = 'Simulation')
	ax.plot(x, y_poisson, label = 'Poisson') #plotting poisson distrubution alongside the histogram of reads
	ax.plot(x, y_normal, label = 'Normal') #Plotting normal distribution
	ax.set_xlabel("Coverage") #label, x axis = coverage 
	ax.set_ylabel("Frequency (bp)") #area under curve = genome length
	ax.legend() #adding in a legend
	fig.tight_layout()
	fig.savefig(figname) #saving as a figure- figure name provided in function



simulate_coverage(3, 1000000, 100, 'ex1_3x_cov.png')  #simulating covering for 3X coverage of 1 Mbp genome length with 100 bp reads. Saving as a figure.
simulate_coverage(10, 1000000, 100, 'ex1_10x_cov.png') #simulating covering for 10X coverage of 1 Mbp genome length with 100 bp reads. Saving as a figure.
simulate_coverage(30, 1000000, 100, 'ex1_30x_cov.png') #simulating covering for 30X coverage of 1 Mbp genome length with 100 bp reads. Saving as a figure.
