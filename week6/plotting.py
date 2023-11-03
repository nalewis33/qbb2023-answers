#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd


#Step 1.2: plotting PCA. 

#results saved as plinkPCA.eigenval and plinkPCA.eigenvec

fig1,ax1  = plt.subplots() #Setting up plot
eigenVectors= 'plinkPCA.eigenvec' #eigenvector dataset
eigenVectors= np.loadtxt(eigenVectors)
PC1 = eigenVectors[:,2] #pulling out PC1 
PC2 = eigenVectors[:,3] #pulling out PC2
ax1.scatter(PC1, PC2, alpha = 0.5, color = 'dodgerblue') #generating a scatter plot of PC1 and PC2
ax1.set_xlabel('PC1') #adding x-axis label
ax1.set_ylabel('PC2') #adding y-axis label
ax1.set_title('Principle Component Analysis of Lymphoblastoid Genotypes') #adding figure title
fig1.savefig('PCA_plot.png') #saving scatter plot as a png file. 
plt.close(fig1) #closing figure


#Exercise 2.1: Computing allele frequencies
#See README.MD for plink calculating of allele frequencies
# allele frequencies saved as allelefreq.frq

allele_freq = pd.read_csv('allelefreq.frq', delim_whitespace = True) #parsing allele frequency data as a pandas df
MAF = allele_freq.loc[:, 'MAF'] #pulling out allele frequency values, under MAF column
fig2, ax2 = plt.subplots() #generating plot
ax2.hist(MAF, bins = 20, color = 'crimson') #generating histogram of allele frequencies
ax2.set_xlabel('Allele Frequency') #adding x-label
ax2.set_ylabel('Count') #adding y-label
ax2.set_title('Alele Frequency Spectrum') #adding title
fig2.savefig('AFS.png') #saving figure as a png file.
plt.close(fig2)

#Exercise 3.2


pheno_GS451 = pd.read_csv('phenotype_gwas_results_GS451.assoc.linear', delim_whitespace = True) #reading in GWAS data for GS451 phenotype
pheno_CB1908 = pd.read_csv('phenotype_gwas_results_CB1908.assoc.linear', delim_whitespace = True) #reading in GWAS data for CB1908 phenotypr

p_val_CB1908 = pheno_CB1908.loc[:,'P'] #pulling out p value columns
p_val_GS451 = pheno_GS451.loc[:, 'P'] #pulling out p value columns
p_val_CB1908_sub = p_val_CB1908[p_val_CB1908 < 1e-5] #finding subset of p-values less than 1e-5
p_val_GS451_sub = p_val_GS451[p_val_GS451 < 1e-5] #finding subset of p-values less than 1e-5

fig3, (ax3, ax4) = plt.subplots(nrows=1, ncols = 2) #setting up figures- includes 2 subplots
ax3.scatter(x = range(len(pheno_GS451)), y = -np.log10(p_val_GS451), color = 'dodgerblue')
ax3.scatter(x = p_val_GS451.index[p_val_GS451 < 1e-5], y = -np.log10(p_val_GS451_sub), color = 'magenta')
ax3.set_ylabel('-log10 p-value')
ax3.set_xlabel('Position')
ax3.set_title('GS451 GWAS')
ax4.scatter(x = range(len(pheno_CB1908)), y = -np.log10(p_val_CB1908), color = 'dodgerblue')
ax4.scatter(x = p_val_CB1908.index[p_val_CB1908 < 1e-5], y = -np.log10(p_val_CB1908_sub), color = 'magenta')
ax4.set_ylabel('-log10 p-value') #adding y label
ax4.set_xlabel('Position') #x label
ax4.set_title('CB1908 GWAS')
fig3.tight_layout() 
fig3.savefig('Manhattan_Plots.png')
plt.close(fig3)


#Exercise 3.3:


#FOR CB1908:
#Identify SNP with smallest p-value (largest -log10pvalue):
SNP_CB1908 = pheno_CB1908['P'].idxmin() #getting index of minimum p-value in phenotype data set
SNP_CB1908 = pheno_CB1908['SNP'].loc[SNP_CB1908] #pulling SNP ID of minimum p-value
#print(SNP_CB1908) #checking SNP

for line in open('genotypes.vcf'):
	if line.startswith('#'): 
		continue #skipping intro lines to move to actual data
	fields = line.rstrip('\n').split('\t')
	if fields[2] == SNP_CB1908: #If this is the SNP with the lowest p-value:
		data = fields[9:] #pull out genotype data (column 10 onwards)

#print(fields)
#print(len(data))

phenotype = [] #empty set for phenotype data
for line in open("CB1908_IC50.txt"):
	fields = line.rstrip('\n').split()
	if fields[2] != 'CB1908_IC50': #skipping header.
		if fields[2] != 'NA': #If IC50 data is a value (not NA/ missing value)
			phenotype.append(float(fields[2])) #add to phenotype data- converting to float
		elif fields[2] == 'NA':
			phenotype.append(fields[2]) #will keep in NA values for now so len of geno and pheno data matches
#print(len(phenotype))

zero_zero = [] #set for 0/0 values
zero_one = []
one_one = []

for i in range(len(data)): #for i in the range of the genotype data:
	if data[i] == '0/0' and phenotype[i] != 'NA': #if genotype is 0/0 and there is a value for phenotype:
		zero_zero.append(phenotype[i])#append to 0/0 set
	elif data[i] == '0/1' and phenotype[i] != 'NA': #if genotype is 0/1 and there is a phenotype value:
		zero_one.append(phenotype[i]) #add to zero_one set
	elif data[i] == '1/1' and phenotype[i] != 'NA': #if genotype is 1/1 and there is a phenotype value:
		one_one.append(phenotype[i])
#print(zero_one)

pheno_sum = [] #creating list for all non-zero values for each genotype
pheno_sum.append(zero_zero) #appending each set on
pheno_sum.append(zero_one)
pheno_sum.append(one_one)

#print(pheno_sum)

genotypes = ['0/0', '0/1', '1/1'] #genotype labels
fig4, ax5 = plt.subplots()
ax5.boxplot(pheno_sum, labels = genotypes) #generating box plot
ax5.set_xlabel('Genotype') #adding x label
ax5.set_ylabel('IC50 (Phenotype)')
ax5.set_title('IC50 rs10876043 by Genotype')
fig4.savefig('CB1908_Boxplot.png')
plt.close(fig4)

#Identifying SNP for GS451 (for exercise 3.4):
SNP_GS451 = pheno_GS451['P'].idxmin() #getting index of minimum p-value in phenotype data set
SNP_GS451 = pheno_GS451['SNP'].loc[SNP_GS451] #pulling SNP ID of minimum p-value
#print(SNP_GS451) #checking SNP