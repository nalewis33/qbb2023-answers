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

#Exercise 2: De Brujin Graph Construction

reads = ['ATTCA', 'ATTGA', 'CATTG', 'CTTAT', 'GATTG', 'TATTT', 'TCATT', 'TCTTA', 'TGATT', 'TTATT', 'TTCAT', 'TTCTT', 'TTGAT'] #adding in list of reads.


"""
Write code to find all of the edges in the de Bruijn graph corresponding to the provided reads using k = 3 
(assume all reads are from the forward strand, no sequencing errors, complete coverage of the genome). 
Each edge should be of the format ATT -> TTC. Write all edges to a file, with each edge as its own line in the file."""

#I'm writing my own psuedocode to help me understand, don't mind me. 
# Create a list of edges (each edge being one line)
# Edge_list = []
# for each element in the reads list:
# 	for i in each element: (ex. 2 edges in a 5 nt sequence, 3 in a 6 nt)
#		first k-mer = letters i- i+2 
#		second k-mer = letter i+1 - i+3
#		edge = k-mer1 --> k-mer 2
#		add edge + \n to Edge_List (to make new line)
#		repeat until finished each edge in each element
# After generating edge list: print each edge on a separate line


#print(reads[0][0]) #calling individual elements (characters) in reads using this formatting (for my own reference)

graph = set() #creating graph, aka set of edges

for sequence in range(len(reads)): #for each sequence in the list of reads
	#print(reads[sequence])
	#sequence_range = range(len(reads[sequence]) - 3)
	#print(type(sequence_range))
	for i in range(len(reads[sequence]) - 3): #for each edge (there are len(nt)- 3 number per sequence when using a k=3):
		kmer1 = (reads[sequence][i:i+3]) #kmer1 = 3 nt based on index
		kmer2 = (reads[sequence][i+1 : i+4])  #kmer 2 = 3 nt, shifted one position over from kmer 1
		#print(kmer1)
		#print(kmer2)
		edge = kmer1 + " -> " + kmer2  #edge = kmer1 -> kmer2
		graph.add(edge) #adding each edge to the graph list
		i+=1 # adding 1 to i
	sequence+=1 #adding 1 to the sequence (reads index)

for edge in graph: #for each edge in the graph
	print(edge) #print each edge. 

#print(graph) #printing to look at


with open('Graph.txt', 'w') as f: #outputting graph to a .txt format that graphviz can read.
	f.write('digraph {\n') #starting with digraph {, introducing a line break
	f.write('\n'.join(graph) ) #adding a line break before each edge 
	f.write('\n}') #concluding text file with another line break and closing bracket. 





