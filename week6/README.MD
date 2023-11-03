Exercise 1.1: 

To run PCA in terminal:
plink --noweb --vcf  genotypes.vcf --pca 10  --out plinkPCA

To get top 10 principal components: 

head -n 10 plinkPCA.eigenvec

Exercise 2.1:

plink --noweb --vcf genotypes.vcf  --freq --out allelefreq


Exercise 3.1:
For CB1908 phenotype:

plink --vcf genotypes.vcf --linear --pheno CB1908_IC50.txt --covar plinkPCA.eigenvec --allow-no-sex --out phenotype_gwas_results_CB1908

For GS451 phenotype:

plink --vcf genotypes.vcf --linear --pheno GS451_IC50.txt --covar plinkPCA.eigenvec --allow-no-sex --out phenotype_gwas_results_GS451

Exercise 3.4:

For CB1908: SNP of interest is rs10876043. 
This SNP is near the DIP2B gene, a transcriptional regulator that is thought to be involved in gene regulation via DNA methylation. This suggests that this variant may have downstream effects on gene expression patterns by altering DNA methylation through variant DIP2B activity. 

For GS451: SNP of interest is rs7257475.

This region surrounds the gene for a zinc finger protein, ZNF826P. Zinc finger proteins frequently contain DNA binding motifs that enable them to bind specific DNA regions and may contribute to downstream events such as gene regulation. Variants in this region may have altered zinc finger activity, affecting it's affinity for binding DNA and altering gene expression as a result. 