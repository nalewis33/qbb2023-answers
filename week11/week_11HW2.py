#!/usr/bin/env python

import sys

import scanpy as sc
import numpy
import matplotlib.pyplot as plt

adata = sc.read_h5ad("filtered_clustered_data.h5") #reading in data generated in week_11HW script 1. 
adata.uns['log1p']['base'] = None # This is needed due to a bug in scanpy 


#Exercise 3.2

#T-cell: CD3D
fig, axes = plt.subplots(ncols = 3, figsize = (10,5))
sc.pl.umap(adata, ax=axes[0], color = 'MS4A1', title="MS4A1 Expression", show=False) #plotting each marker- should be representative of B cells
sc.pl.umap(adata, ax=axes[1], color = 'PPBP', title="PPBP Expression", show=False) #plotting each marker- should be representative of megakaryocytes. 
sc.pl.umap(adata, ax=axes[2], color = 'IL7R', title="IL7R Expression", show=False) #plotting each marker- should be representative of CD4 T cells.
plt.tight_layout()
plt.savefig("Gene_Cluster.png") #saving as PNG
plt.close()

#Exercise 3.3:

cluster_names = ['CD4 T cells', ' ','B cells', '  ','   ', '     ','       ', 'Megakaryocytes'] #adding in labels- need to add labels for every cluster, so I left them as blank spaces
adata.rename_categories('leiden', cluster_names) #renaming clusters based on cluster name set. 
sc.pl.umap(adata, color='leiden', legend_loc='on data', title='', frameon=False, save='.pdf') #plotting UMAP with cluster names
