#!/usr/bin/env python

import sys
from model_peaks import load_bedgraph, bin_array, find_correlations, find_profile, find_peaks #importing functions from model_peaks generated in class
import numpy as np
import scipy.stats
import matplotlib.pyplot as plt


def main():
    # Load file names and fragment width
    forward_fname, reverse_fname, ctrlforward_fname, ctrlreverse_fname, f_width, output_bed, output_wig = sys.argv[1:8] #defining variables to be supplied by user- including forward/reverse sequences (including control), output files, and fragment width (198)
    f_width = int(f_width) # converting f_width to an integer- as read in by sys.argv, currently a string. 

    # Define what genomic region we want to analyze
    chrom = "chr2R"
    chromstart = 10000000
    chromend =  12000000
    chromlen = chromend - chromstart
  

    # Load the sample bedgraph data, reusing the function we already wrote
    
    forward = load_bedgraph(forward_fname, chrom, chromstart, chromend) #loading in forward data
    reverse = load_bedgraph(reverse_fname, chrom, chromstart, chromend) #loading in reverse data

    # Combine tag densities, shifting by our previously found fragment width
    
    sample = np.zeros(chromlen, dtype = int) #genearting sample array of zeroes the length of the chromosome region  
    #print(sample) # printing to look at
    sample[f_width//2:] += forward[:-f_width//2] #shifting the left side (starting from beginning) by f_width/2 base pairs
    sample[:-f_width//2] = reverse[f_width//2:]  #shifting the right side (starting from end of chromosome) by f_width/2 base pairs (each side shifted by 1/2 f_width to get total shift)
    #print(sample) #printing to look at

    # Load the control bedgraph data, reusing the function we already wrote
    
    ctrl_forward = load_bedgraph(ctrlforward_fname, chrom, chromstart, chromend)
    ctrl_reverse = load_bedgraph(ctrlreverse_fname, chrom, chromstart, chromend)

    # Combine tag densities
    ctrl_combined = ctrl_forward + ctrl_reverse

    # Adjust the control to have the same coverage as our sample

    sum_sample = np.sum(sample) #sum of coverage in sample
    sum_ctrl = np.sum(ctrl_combined) #sum of coverage in control set
    #print(sum_sample)
    #print(sum_ctrl)
    adjustment = sum_sample/sum_ctrl  #adjustment factor 
    ctrl_combined = ctrl_combined * adjustment 

    # Create a background mean using our previous binning function and a 1K window
    # Make sure to adjust to be the mean expected per base

    background_mean = (bin_array(ctrl_combined, 1000))/1000 #using bin_array function to create the background mean, then dividing results by 1000 to get mean per base (divide by 1000 since window is 1kb)
    #print(background_mean) #printing to look at

    # Find the mean tags/bp and make each background position the higher of the
    # the binned score and global background score
    ctrl_mean = int(np.mean(ctrl_combined))
    background_mean = np.max(background_mean, ctrl_mean) #setting the background mean score to the higher of the values- background mean calculated from the binning function or the mean of the ctrl_combined set

    # Score the sample using a binsize that is twice our fragment size
    # We can reuse the binning function we already wrote

    binsize = f_width * 2 #defining binsize as 2* fragment width
    score = bin_array(sample, binsize) 

    # Find the p-value for each position (you can pass a whole array of values
    # and and array of means). Use scipy.stats.poisson for the distribution.
    # Remeber that we're looking for the probability of seeing a value this large
    # or larger
    # Also, don't forget that your background is per base, while your sample is
    # per 2 * width bases. You'll need to adjust your background

    p_val = (1 - scipy.stats.poisson.cdf(score, background_mean*(2*f_width))) #calculating p value using scipu.stats.poisson. Adjusting background to match score

    # Transform the p-values into -log10
    # You will also need to set a minimum pvalue so you doen't get a divide by
    # zero error. I suggest using 1e-250
    p_val = np.maximum(p_val, 1e-250) #converting to log 10- if p_val less than 1e-250, will use 1e-250 as minimum p-value. 
    p_val_log10 = -np.log10(p_val) #making it the negative log value 
    # Write p-values to a wiggle file
    # The file should start with the line
    # "fixedStep chrom=CHROM start=CHROMSTART step=1 span=1" where CHROM and
    # CHROMSTART are filled in from your target genomic region. Then you have
    # one value per line (in this case, representing a value for each basepair).
    # Note that wiggle files start coordinates at 1, not zero, so add 1 to your
    # chromstart. Also, the file should end in the suffix ".wig"

    write_wiggle(p_val_log10, chrom, chromstart, output_wig) #writing to output_wig file, defined by user in terminal

    # Write bed file with non-overlapping peaks defined by high-scoring regions 
    write_bed(score, chrom, chromstart, chromend, f_width, output_bed) #writing to output_bed file, defined by user in terminal 

def write_wiggle(pvalues, chrom, chromstart, fname):
    output = open(fname, 'w')
    print(f"fixedStep chrom={chrom} start={chromstart + 1} step=1 span=1",
          file=output)
    for i in pvalues:
        print(i, file=output)
    output.close()

def write_bed(scores, chrom, chromstart, chromend, width, fname):
    chromlen = chromend - chromstart
    output = open(fname, 'w')
    while np.amax(scores) >= 10:
        pos = np.argmax(scores)
        start = pos
        while start > 0 and scores[start - 1] >= 10:
            start -= 1
        end = pos
        while end < chromlen - 1 and scores[end + 1] >= 10:
            end += 1
        end = min(chromlen, end + width - 1)
        print(f"{chrom}\t{start + chromstart}\t{end + chromstart}", file=output)
        scores[start:end] = 0
    output.close()


if __name__ == "__main__":
    main()
