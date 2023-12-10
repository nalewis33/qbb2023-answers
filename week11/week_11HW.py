#!/usr/bin/env python

import sys

import scanpy as sc
import numpy
import matplotlib.pyplot as plt

#Exercise 0
# Read the 10x dataset filtered down to just the highly-variable genes
adata = sc.read_h5ad("variable_data.h5")
adata.uns['log1p']['base'] = None # This is needed due to a bug in scanpy 

#Exercise 1.1: Computing a neighborhood graph
sc.pp.neighbors(adata, n_neighbors = 10, n_pcs = 40)

#Exercise 1.2: Leiden Clustering

sc.tl.leiden(adata)

#Exercise 1.3: UMAP and t-SNE

sc.tl.umap(adata, maxiter=900)
sc.tl.tsne(adata)

"""
fig, axes = plt.subplots(ncols = 2, figsize = (10,5))
sc.pl.umap(adata, ax=axes[0], color = 'leiden', title="UMAP", show=False)
sc.pl.tsne(adata, ax=axes[1], color = 'leiden', title="tSNE", show=False)
plt.tight_layout()
plt.savefig("UMAP_tSNE.png")
plt.close()
"""

#Exercise 2.1 

wilcoxon_adata = sc.tl.rank_genes_groups(adata,  method = 'wilcoxon',  groupby = 'leiden', use_raw=True, copy=True)
logreg_adata = sc.tl.rank_genes_groups(adata,  method = 'logreg',  groupby = 'leiden', use_raw=True, copy=True)

#Exercise 2.2

sc.pl.rank_genes_groups(wilcoxon_adata, n_genes = 25, title = 'Top 25 Genes- Wilcoxon', sharey=False, show=False, use_raw=True, save = 'wilcoxon.png')
sc.pl.rank_genes_groups(logreg_adata, n_genes = 25,  title = 'Top 25 Genes- Logreg', sharey=False, show=False, use_raw=True, save = 'logreg.png')
plt.tight_layout()
plt.savefig("Wilcoxon_Logreg.png")
plt.close()

leiden = adata.obs['leiden']
umap = adata.obsm['X_umap']
tsne = adata.obsm['X_tsne']
adata = sc.read_h5ad('filtered_data.h5')
adata.obs['leiden'] = leiden
adata.obsm['X_umap'] = umap
adata.obsm['X_tsne'] = tsne

adata.write('filtered_clustered_data.h5')