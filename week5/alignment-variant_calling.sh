#!/bin/bash

#echo "Hello, world!" #testing to make sure file initialized

#Step 1.1: Indexing the SacCer genome
bwa index sacCer3.fas #indexing. 

#Step 1.2: Aligning each of our 10 reads to the index using bwa mem
for sample in A01_09 A01_11 A01_23 A01_24 A01_27 A01_31 A01_35 A01_39 A01_62 A01_63 #for each of the 10 alignment samples: 
do
	echo "Aligning sample: " ${sample} #adding in a title of "Aligning sample:" + whatever sample is being aligned. 
	bwa mem -t 4 -R "@RG\tID:${sample}\tSM:${sample}"\
	 sacCer3.fa \
	${sample}.fastq > ${sample}.sam # -R to add appropriate sample header, and -t to speed up process. Outputting each file to a sam file. 
	samtools sort ${sample}.sam -O bam -o ${sample}.bam #sorting and outputting as bam file
	samtools index ${sample}.bam -M -o ${sample}.bam.bai #indexing the sorted bam files, outputting as a bam.bai 
done

freebayes -f SacCer3.fa -p 1 --genotype-qualities A01_09.bam A01_11.bam A01_23.bam A01_24.bam A01_27.bam A01_31.bam A01_35.bam A01_39.bam A01_62.bam A01_63.bam>var.vcf #identifying genetic variants across the strains concurrently using freebase. 


vcffilter var.vcf -f "QUAL > 20" > filtered_var.vcf #filtering based on Phred value (0.99 chance = QUAL >20)

vcfallelicprimitives filtered_var.vcf -k -g > var_prim.vcf #filtering

snpEff ann R64-1-1.105 var_prim.vcf > ann_vcf.vcf #annotating relative to the reference genome

head -n 100 ann_vcf.vcf > samplevcf.vcf #generating sample vcf- making the first 100 lines in order to include the first 100 actual rows of data

