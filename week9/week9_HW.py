#!/usr/bin/env python

import numpy as np
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf
from statsmodels.stats import multitest
from pydeseq2 import preprocessing
from pydeseq2.dds import DeseqDataSet
from pydeseq2.ds import DeseqStats
import matplotlib.pyplot as plt

# read in data
counts_df = pd.read_csv("gtex_whole_blood_counts_formatted.txt", index_col = 0)

# read in metadata
metadata = pd.read_csv("gtex_metadata.txt", index_col = 0)

#print(counts_df)
#print(metadata)

counts_df_normed = preprocessing.deseq2_norm(counts_df)[0]

counts_df_normed = np.log2(counts_df_normed + 1)


full_design_df = pd.concat([counts_df_normed, metadata], axis=1)

print(full_design_df)



columns = ['Gene', 'Slope', 'P-value'] #generating header columns for dataset

gene_results = pd.DataFrame(columns = columns) #creating empty df for the results with the column headers specified
gene_list = counts_df_normed.columns #defining gene list based on columns from counts_df_normed
#print(gene_list) #printing to look at

for gene in gene_list: #for each column in data frame (to run for each gene)
	model = smf.ols(formula = f'Q("{gene}") ~ SEX', data = full_design_df)
	results = model.fit()
	slope = results.params[1] #pulling out slope
	pval = results.pvalues[1] #pulling out p value
	gene_results.loc[len(gene_results), :] = [gene, slope, pval] #appending each calculated row to the dataframe.

gene_results.to_csv('Results.txt', header= True, index= False, sep = '\t') #exporting dataset to a text file.



gene_pre_results = pd.read_csv('Results.txt', sep = '\t', header= 0, index_col= 0) #importing in previous result file just so I can skip rerunning the df generation- it's too slow >:( 
#its pre_results because these are the results before filtering out the p-values, it made more sense in my head

gene_pre_results['P-value'] = gene_pre_results['P-value'].fillna(1.0) #removing nan value 

p_value_corrected = multitest.fdrcorrection(gene_pre_results['P-value'], alpha = 0.05, method = 'indep', is_sorted = False) #running FDR correction on p-values 
p_value_corrected_out = p_value_corrected[1] #pulling out adjusted p-values

#print(p_value_corrected_out) #looking at pulled out p-values

fdr_columns = ['P-value']
fdr_genes = pd.DataFrame(p_value_corrected_out, index = gene_pre_results.index, columns = fdr_columns) #adding genes to df
#print(fdr_genes)


fdr_final = fdr_genes.loc[(fdr_genes['P-value'] <= 0.1)] #final gene set with 10% FDR (p <= 0.1)
fdr_final.to_csv('1.5_FDR_Transcripts.txt', header = True, sep = '\t') #exporting to csv

#print(fdr_final) #printing to look at



#Exercise 2:

dds = DeseqDataSet(
    counts=counts_df,
    metadata=metadata,
    design_factors="SEX",
    n_cpus=4,
)

dds.deseq2()
stat_res = DeseqStats(dds)
stat_res.summary()
results = stat_res.results_df

#print(results)


Deseq_sig = results.loc[(results['padj'] <0.1)]
Deseq_sig.to_csv('Deseq_sig_transcripts.txt', header = True, sep = '\t')


#Calculate Jaccard index:
#((number of genes that were significant in steps 1 and 2) / (number of genes that were significant in steps 1 or 2)) * 100%


fdr_genes = set() #empty set to add genes ID'd by manual FDR
for line in open('1.5_FDR_Transcripts.txt'): #reading each line in transcripts ID's by manual FDR
	gene = line.rstrip('\n').split('\t')[0] #Gene = index column being stripped (getting just gene name, not p value)
	fdr_genes.add(gene) #adding to fdr_gene set
 
Deseq_genes = set() #empty set to add genes ID'd by Deseq
for lines in open('Deseq_sig_transcripts.txt'): #opening Deseq text file and reading each line
	gene = lines.rstrip('\n').split('\t')[0] #pulling out index column with gene names
	Deseq_genes.add(gene) #adding to Deseq_genes set
  
#print(fdr_genes) #printing to look at
#print(Deseq_genes) #printing to look at

overlap = Deseq_genes.intersection(fdr_genes) #overlap between both sets
fdr_unique = fdr_genes.difference(Deseq_genes) #getting the set of genes unique to fdr
Deseq_genes_unique = Deseq_genes.difference(fdr_genes) #set of genes unique to Deseq

#print(len(fdr_unique)) #printing to look at
#print(len(Deseq_genes_unique)) #printing to look at
#print(len(overlap)) #printing to look at

Jaccard = len(overlap)/(len(overlap)+len(fdr_unique)+len(Deseq_genes_unique)) * 100 #calculating jaccard index- to avoid repeats between both sets, adding in the overlap and then the unique genes in each set. 
print(f"The Jaccard index is {Jaccard}%.") #printing index to add into README.md file

#Exercise 3: 
"""
Use matplotlib to create a “Volcano” plot depicting your differential expression results from Exercise 2. A volcano plot is a scatter plot, 
where the x-axis shows the log2FoldChange and the y-axis shows the -log10(padj).

Highlight the genes that are significant at a 10% FDR AND for which the absolute value of the log2FoldChange is greater than 1 in a separate color.

Output this plot to a .png that you will upload with your assignment.
"""

log2FoldChange = [] #creating empty set for log2FoldChange values
padjlog10 = [] #creating empty set for -log10padj values

for lines in open('Deseq_sig_transcripts.txt'): #opening Deseq text file and reading each line
	log2change = lines.rstrip('\n').split('\t')[2] #pulling out index column with gene names
	if log2change == 'log2FoldChange':
		continue #skipping header
	else:
		log2FoldChange.append(float(log2change))
	padj = lines.rstrip('\n').split('\t')[6]
	if padj == 'padj': #skipping header
		continue
	elif padj == '0.0':
		padj = 1 #changing 1 to 0s to nplog10 works, will go to 0
		padjlog10.append(padj)#adding in value
	else:
		padjlog10.append(padj) #adding in value

for i in range(len(padjlog10)):
	padjlog10[i] = float(padjlog10[i])
	padjlog10[i] = -np.log10(padjlog10[i]) #converting padj to -log10

Volcano_set = pd.DataFrame({'log2FoldChange' : log2FoldChange, '-log10(padj)':padjlog10}) #merging into a dataframe
#print(Volcano_set)

Volcano_subset =  Volcano_set[abs(Volcano_set['log2FoldChange']) >= 1] #pulling values with absolute log2FoldChange greater than 1
#print(Volcano_subset['log2FoldChange'])



fig, ax = plt.subplots() #creating figures
ax.scatter(x = Volcano_set['log2FoldChange'], y = Volcano_set['-log10(padj)'], color= 'dodgerblue') #adding in total set of data points
ax.scatter(x = Volcano_subset['log2FoldChange'], y = Volcano_subset['-log10(padj)'], color = 'magenta') #adding in highlight points
ax.set_xlabel('log2FoldChange') #setting x label title
ax.set_ylabel('-log10(padj)') #setting y label title
ax.set_title('Volcano Plot of Differential Expression')
fig.savefig('Volcano_plot.png') #saving figure as a png
plt.close()