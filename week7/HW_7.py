#!/usr/bin/env python

import sys
import matplotlib.pyplot as plt
import numpy as np

"""

Part 3a

Using the above bedgraph files, write a Python script to perform a number of comparisons between the two sets of methylation calls. Your script should be able to:

Parse the bedgraph files
Calculate the number of sites present only in the bismark file, present only in the nanopore file, and the shared sites as a percentage of total sites (both unique and shared sites) and record them in your README.md file.

"""

def load_data(fname):
    data = []
    for line in open(fname):
        line = line.rstrip().split()
        data.append([
            int(line[1]), float(line[3]), int(line[4])]) #pulling out bp, methyaltion percentage, and num reads
    return  data


bisulfite = load_data('bisulfite.cpg.chr2.bedgraph')
nanopore = load_data('ONT.cpg.chr2.bedgraph')
bisulfite_set = set()
nanopore_set = set()
bisulfite_unique = set()
nanopore_unique = set()
overlap= set()

# Find reads that appear in both datasets

for i in range(len(bisulfite)):
    if bisulfite[i][0] not in bisulfite_unique: #add bisulfite reads to unique reads for bisulfite
    	bisulfite_set.add(bisulfite[i][0])


for i in range(len(nanopore)):
	if nanopore[i][0] in bisulfite_set:
		overlap.add(nanopore[i][0])
		nanopore_set.add(nanopore[i][0])
	elif nanopore[i][0] not in bisulfite_unique:
		nanopore_unique.add(nanopore[i][0])

bisulfite_unique = bisulfite_set.difference(overlap)

total_methylation = (len(overlap)) + (len(bisulfite_unique)) + len(nanopore_unique)
print(f"The number of sites unique to the bisulfite file is {len(bisulfite_unique)}, which is {len(bisulfite_unique)/(total_methylation) * 100}% of total methylation sites.")
print(f"The number of sites unique to the nanopore sequencing file is {len(nanopore_unique)}, which is {len(nanopore_unique)/(total_methylation) * 100}% of total methylation sites.")
print(f"The number of sites shared between the two files is {len(overlap)}, which is {len(overlap)/(total_methylation) * 100}% of total methylation sites.")


"""
3b:
Plot the distribution of coverages across CpG sites for each track on the same plot.
Make sure to indicate which distribution corresponds to which track. 
In order to visualize both distributions on the same plot, 
it may be useful to use the alpha option to set the transparency of the plotted data.
"""


nanopore_reads = []
nano_bp = []
for i in range(len(nanopore)):
	nano_bp.append(nanopore[i][0]) #pulling out methylated bp 
	nanopore_reads.append(nanopore[i][2]) #pulling out read number

bisulfite_reads = []
bisulfite_bp = []
for i in range(len(bisulfite)):
	bisulfite_bp.append(bisulfite[i][0]) #pulling out methylated bp
	bisulfite_reads.append(bisulfite[i][2]) #pulling out read number

"""
fig, ax = plt.subplots()
ax.scatter(x = nano_bp, y = nanopore_reads, color='dodgerblue', alpha = 0.0075, label = 'Nanopore')
ax.scatter(x = bisulfite_bp, y = bisulfite_reads, color = 'crimson', alpha = 0.0075, label = 'Bisulfite')
ax.set_xlabel('Location')
ax.set_ylabel('Coverage')
ax.set_title('Distribution of Bisulfite and Nanopore Coverage at CpG Islands')
ax.legend()
plt.savefig('Coverage_Dist.png')
plt.close(fig)
"""

"""
3C:
For CpG sites occurring in both bedgraph files, plot the relationship between methylation scores 
for the two approaches. Because of the number of data points, it is impractical to do this 
using a scatterplot. Instead, use the numpy function histogram2d and plot using the 
matplotlib function imshow. I recommend 100 bins per axis for the histogram as this will 
make the axis labels match the percent methylation.

To do this, first run numpy.histogram2d() on your data. 
numpy.histogram2d() returns three items - a histogram, the x edges and the y edges. 
Store the histogram as a variable. Because points are highly concentrated in the corners, 
it is difficult to see much of the data. Therefore you should transform the histogram using a 
log10(data + 1) transformation. Plot your transformed histogram imshow().

You also should calculate the Pearson R coefficient for the two sets of methylation calls
(non-transformed data). This is easy to do using the numpy function corrcoef. 
Include this value in the title (no more than 3 decimal places, please).

"""

nanopore_overlap=[]
bisulfite_overlap = []

for i in range(len(nanopore)):
	if nanopore[i][0] in overlap: #if this bp was in the overlap region:
		nanopore_overlap.append([nanopore[i][0], nanopore[i][1]]) #pulling out bp and methylation score
#print(nanopore_overlap)

for i in range(len(bisulfite)):
	if bisulfite[i][0] in overlap: #if this bp was in the overlap region:
		bisulfite_overlap.append([bisulfite[i][0], bisulfite[i][1]]) #pulling out bp and methylation score
#print(bisulfite_overlap)

nanopore_meths = []
nano_bp_o = []
for i in range(len(nanopore_overlap)): #pulling out overlapping reads + methylation scores for methylated CpG in naopore
	nano_bp_o.append(nanopore_overlap[i][0])
	nanopore_meths.append(nanopore_overlap[i][1])

bisulfite_meths = []
bisulfite_bp_o = []
for i in range(len(bisulfite_overlap)): #pulling out reads + methylation scores for methylated CpG in bisulfite data
	bisulfite_bp_o.append(bisulfite_overlap[i][0])
	bisulfite_meths.append(bisulfite_overlap[i][1])



nano_hist, x_edge, y_edge = np.histogram2d(nano_bp_o, nanopore_meths, bins = 100) #setting up nanopore sequencing 2D histogram
bis_hist, x_edge_b, y_edge_b = np.histogram2d(bisulfite_bp_o, bisulfite_meths, bins = 100) #setting up bisulfite 2D hist 

nano_hist = np.log10(nano_hist + 1) #transforming by log10(data + 1)
bis_hist = np.log10(bis_hist + 1) #transforming by log10(data + 1)

r_coeff = np.corrcoef(nanopore_meths, bisulfite_meths) #correlation calculation on methylation scores
#print(r_coeff)

"""
fig2,ax2 = plt.subplots() #setting up plot
plt.imshow(nano_hist, alpha = 0.5)
plt.imshow(bis_hist, alpha = 0.5)
ax2.set_title('Nanopore vs. Bisulfite Methylation: R = 0.936')
plt.savefig('2DHistogram.png')

"""
"""
Now, let’s examine the matched normal-tumor samples. You should be able to load these 
bedgraph files with the same parser as the previous files. 
For each pair of samples (normal and tumor), for all CpG sites in common 
find the change in methylation (tumor - normal), excluding values with no change.
 Create a violin plot showing the distribution of methylation changes, 
 one distribution for nanopore and one for bisulfite results. 
 Using common sites between the two approaches, find the Pearson R coefficient for 
 methylation changes and add this value to the title of the plot.

Q3: What can you infer about the two different approaches and their ability to detect 
methylation changes? 
Q4: What is the effect of tumorigenesis on global methylation patterns?

"""

normal_bis = load_data('normal.bisulfite.chr2.bedgraph') #loading in normal tissue bisulfite data
normal_nano = load_data('normal.ONT.chr2.bedgraph') #loading in normal tissue nanopore data

tumor_bis = load_data('tumor.bisulfite.chr2.bedgraph') #loading in tumor bisulfite
tumor_nano = load_data('tumor.ONT.chr2.bedgraph') #loading in tumor nanopore data

#Look at changes in methylation rate for sites that overlap: 

#Overlapping in bisulfite data: 
bisulfite_overlap_cells = set()
bis_n = set() 
bis_t = set()

for i in range(len(normal_bis)):
    if normal_bis[i][0] not in bis_n: 
    	bis_n.add(normal_bis[i][0]) #adding all nomal bisulfite reads into a set


for i in range(len(tumor_bis)):
	if tumor_bis[i][0] in bis_n: #if tumor bisulfite reads appear in normal bisulfite reads (overlap)
		bisulfite_overlap_cells.add(tumor_bis[i][0]) #add into overlap data set. 
		bis_t.add(tumor_bis[i][0])

#Pulling out methylation data for overlaps: 

bisulfite_meth_overlap_n = []

for i in range(len(normal_bis)):
	if normal_bis[i][0] in bisulfite_overlap_cells: #if this bp was in the overlap region:
		bisulfite_meth_overlap_n.append([normal_bis[i][0], normal_bis[i][1]]) #pulling out bp and methylation score

bisulfite_meths_n = []
bisulfite_bp_o_n = []
for i in range(len(bisulfite_meth_overlap_n)): #pulling out reads + methylation scores for methylated CpG in bisulfite data
	bisulfite_bp_o_n.append(bisulfite_meth_overlap_n[i][0])
	bisulfite_meths_n.append(bisulfite_meth_overlap_n[i][1])

bisulfite_meth_overlap_t = []
for i in range(len(tumor_bis)):
	if tumor_bis[i][0] in bisulfite_overlap_cells: #if this bp was in the overlap region:
		bisulfite_meth_overlap_t.append([tumor_bis[i][0], tumor_bis[i][1]]) #pulling out bp and methylation score

bisulfite_meths_t = []
bisulfite_bp_o_t = []
for i in range(len(bisulfite_meth_overlap_t)): #pulling out reads + methylation scores for methylated CpG in bisulfite data
	bisulfite_bp_o_t.append(bisulfite_meth_overlap_t[i][0])
	bisulfite_meths_t.append(bisulfite_meth_overlap_t[i][1])



#Overlapping in nanopore data:

nano_overlap_cells = set()
nano_n = set() 
nano_t = set()

for i in range(len(normal_nano)):
    if normal_nano[i][0] not in nano_n: 
    	nano_n.add(normal_nano[i][0]) #adding all nomal nano reads into a set


for i in range(len(tumor_nano)):
	if tumor_nano[i][0] in nano_n: #if tumor bisulfite reads appear in normal bisulfite reads (overlap)
		nano_overlap_cells.add(tumor_nano[i][0]) #add into overlap data set. 
		nano_t.add(tumor_nano[i][0])

#Pulling out methylation data for overlaps: 

nano_meth_overlap_n = []

for i in range(len(normal_nano)):
	if normal_nano[i][0] in nano_overlap_cells: #if this bp was in the overlap region:
		nano_meth_overlap_n.append([normal_nano[i][0], normal_nano[i][1]]) #pulling out bp and methylation score

nano_meths_n = []
nano_bp_o_n = []
for i in range(len(nano_meth_overlap_n)): #pulling out reads + methylation scores for methylated CpG in bisulfite data
	nano_bp_o_n.append(nano_meth_overlap_n[i][0])
	nano_meths_n.append(nano_meth_overlap_n[i][1])

nano_meth_overlap_t = []
for i in range(len(tumor_nano)):
	if tumor_nano[i][0] in nano_overlap_cells: #if this bp was in the overlap region:
		nano_meth_overlap_t.append([tumor_nano[i][0], tumor_nano[i][1]]) #pulling out bp and methylation score

nano_meths_t = []
nano_bp_o_t = []
for i in range(len(nano_meth_overlap_t)): #pulling out reads + methylation scores for methylated CpG in bisulfite data
	nano_bp_o_t.append(nano_meth_overlap_t[i][0])
	nano_meths_t.append(nano_meth_overlap_t[i][1])

"""
fig3, ax3 = plt.subplots()
ax3.violinplot([bisulfite_meths_t, bisulfite_meths_n, nano_meths_t, nano_meths_n])
ax3.set_title('Changes in Methylation in Tumor Cells and Sequencing Methods')
ax3.set_ylabel('Methylation Coverage')
ax3.set_xticks(['Bisulfite, Tumor','Bisulfite, Normal','Nanopore, Tumor','Nanopore, Normal'])
plt.savefig('Violinplot.png')
"""


fig4, ax4 = plt.subplots(nrows=1, ncols = 3, figsize=(10,10))
ax4[0].scatter(x = nano_bp, y = nanopore_reads, color='dodgerblue', alpha = 0.0075, label = 'Nanopore')
ax4[0].scatter(x = bisulfite_bp, y = bisulfite_reads, color = 'crimson', alpha = 0.0075, label = 'Bisulfite')
ax4[0].set_xlabel('Location')
ax4[0].set_ylabel('Coverage')
ax4[0].set_title('Distribution of Bisulfite and Nanopore Coverage at CpG Islands')
ax4[0].legend()
ax4[1].imshow(nano_hist, alpha = 0.5)
ax4[1].imshow(bis_hist, alpha = 0.5)
ax4[1].set_title('Nanopore vs. Bisulfite Methylation: R = 0.936')
ax4[2].violinplot([bisulfite_meths_t, bisulfite_meths_n, nano_meths_t, nano_meths_n])
ax4[2].set_title('Changes in Methylation in Tumor Cells and Sequencing Methods')
ax4[2].set_ylabel('Methylation Coverage')
plt.tight_layout()
plt.savefig('CombinedPlots.png')