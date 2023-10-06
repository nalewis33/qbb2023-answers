#!/usr/bin/env python
import numpy as np 
import sys
import pandas as pd

from fasta import readFASTA

#actually aligning the DNA will take a while- try the code out first with test sequences(or try with the amino acid sequence) before running the entire thing. 

fasta_file = sys.argv[1] #setting up sys.argv- fasta_file will be provided by user in command line. 
scoring_matrix = sys.argv[2] #setting up sys.argv to accept the scoring matrix provided by user.
gap_penalty = int(sys.argv[3]) #setting up sys.argv to accept the gap penalty provided by user- converting it to a float to make sure it's a numerical value and not a string. 
file_name = sys.argv[4]# setting up sys.argv to accept a file name procided by the user- this will be used to save alignment data. 

input_sequences = readFASTA(open(fasta_file)) #using readFASTA function to parse out data
#print(input_sequences) #printing input_sequences to check


seq1_id, sequence1 = input_sequences[0] # defining sequence 1 ID, sequence 1 itself
seq2_id, sequence2 = input_sequences[1] #defining sequence 2 ID, sequence 2 itself

#print(seq1_id)
#print(sequence1)
#print(type(seq1_id))
#print(type(sequence1))
#print(sequence2)
#print(seq2_id)

#sequence1 = 'TGTTACGG' #Test sequences
#sequence2 = 'GGTTGACTA' #Test sequences

scoring_matrix_df = pd.read_csv(scoring_matrix, sep = '\s+') #converting scoring matrix into a df we can use, separating by variable white space. 

#print(scoring_matrix_df) #printing scoring matrix to check spacing

F_matrix = np.zeros((len(sequence1)+ 1, len(sequence2) +1)) #generating F-matrix
#print(F_matrix) #printing to check


for i in range(len(sequence1)+ 1): #Adding in gap penalty row
	F_matrix[i, 0] = i * gap_penalty

for j in range(len(sequence2)+ 1): #Adding in gap penalty column
	F_matrix[0, j] = j * gap_penalty

#print(F_matrix) #printing to check population of gap row + column

traceback_matrix = np.zeros((len(sequence1)+ 1, len(sequence2) +1), dtype='str')  #generating traceback matrix- need to make string values with dtype
#filling in rows of F_matrix

for i in range(1, F_matrix.shape[0]): #for row position starting at index 1 (skipping gap penalty row)
	for j in range(1, F_matrix.shape[1]):  #for column position starting at index 1 (skipping gap penalty column)
		match_score =  scoring_matrix_df.loc[sequence1[i-1], sequence2[j-1]] #match score provided by the match/mismatch table provided by user (HOXD or BLOSUM62)- pulls value based on sequence1 and sequence2 bp/AA values
		d = F_matrix[i-1, j-1] + match_score #diagonal score = sum from previous + match/mismatch score
		h = F_matrix[i, j-1] + gap_penalty #horizontal value = sum from previous (position 1 to the left) + gap penalty (provided by user)
		v = F_matrix[i-1, j] + gap_penalty #vertical value = sum from precious (position 1 up) + gap penalty (provided by user)
		F_matrix[i, j] = max(d, h, v) #value that populates the matrix is the max from the three options. 

print(F_matrix) #printing to look at 


#Psuedo code for traceback matrix:
#Starting at final posiiton of matrix (let's say [i, j]):
# If i-1, j-1 is the greatest: add a 'd' for diagonal to matrix
# If i-1, j is the greatest: add a 'v' for vertical to matrix
# If i, j-1 is the greatest: add a 'h' for horizontal to matrix.
# If there is a tie, favor in this order: aligning (diagonal), gap in sequence 1 (h), gap in sequence 2 (v)

i = len(sequence1)  #starting off traceback matrix by defining values to begin with (value at last row, last column)- row position
j = len(sequence2)  #starting off traceback matrix by defining values to begin with (value at last row, last column)- column position

#Populating the traceback matrix- starting at last row, last column value and working backwards. 

while i != -1 and j != -1: #before you hit the very last position of the matrix (position [0,0]):
	d = F_matrix[i-1, j-1] #setting diagonal position = the position in the F-matrix horizontal
	h = F_matrix[i, j-1] #defining horizontal position 
	v = F_matrix[i-1, j] #defining vertical position
	if max(d, v, h) == d: #if diagonal is the greatest value
		traceback_matrix[i, j] = 'd' #set value in traceback matrix to d
		i -= 1 #move up one
		j -= 1 #move over one
	elif max(d, v, h) == v: #if vertical is greatest:
		traceback_matrix[i, j] = "v" #set traceback matrix position to v
		i -=1 #move up one
	elif max(d, v, h) == h: #if greatest value is horizontal:
		traceback_matrix[i, j] = 'h' #set traceback matrix position to h
		j -= 1 #move over one
	elif max(d, v, h) == d and h: #if the max is the diagonal and horizontal (AKA they're equal):
		traceback_matrix[i, j] = 'd' #pick the diagonal value for populating traceback matrix
		i -= 1 #move up one
		j -= 1 #move over one
	elif max(d, v, h) == d and v: #if the max is the diagonal and vertical (AKA they're equal):
		traceback_matrix[i, j] = 'd' #pick the diagonal for populating traceback
		i -= 1 #move up one
		j -= 1 #move over one
	elif max(d, v, h) == v and h: #if the max is the horizontal and vertical (AKA they're equal):
		traceback_matrix[i, j] = 'h' #pick the horizontal (gap in sequence 1) for populating traceback
		i -= 1 #move up one

print(traceback_matrix) #print the traceback matrix to look at it.

#Exercise 1.4

#Generate the alignment:
#Use traceback matrix to generate the alignment. 
# If diagonal: match (sequence1[bp/AA] = sequence2[bp/AA])
# If horizontal: sequence 2 aa, sequence 1 = gap
# If vertical: sequence1 aa, sequence 2 = gap

sequence1_align = "" #generating empty alignment for sequence1- this will be added to using while loop
sequence2_align = "" #generating empty alignment for sequence2- this will be added to using while loop

row = len(sequence1)  #defining row as the last value in sequence 1 
col = len(sequence2)  #defining column as the last value in sequence 2
#print(row)
#print(col)
#print(traceback_matrix[row, col])


while row > 0 and col > 0:  #before we hit the starting index in the matrices (F_matrix[0,0])
#Note: since working backwards on alignment, need to add new positions in front of the generated alignment  (new bp/AA/gap + sequence alignment)
	if traceback_matrix[row, col] == 'd':
		sequence1_align = sequence1[row-1] + sequence1_align #adding alignment of sequence 1 on- adding new bp/AA+ previously calculated alignment
		sequence2_align = sequence2[col-1] + sequence2_align #adding alignment of sequence 2 on= adding new bp/AA+ previously calculated alignment
		row -= 1 #move one row up
		col -= 1 #move one column over
	elif traceback_matrix[row, col] == 'h': #if horizontal in traceback:
		sequence1_align = "-" + sequence1_align #add gap to sequence 1 alignment (preferred over sequence 2)
		sequence2_align = sequence2[col-1] + sequence2_align #add new bp/AA to sequence 2 alignment
		col -= 1 #move one column over
	elif traceback_matrix[row, col] == 'v': #if vertical in traceback:
		sequence1_align = sequence1[row-1] + sequence1_align #add new bp/AA to sequence 2 alignment
		sequence2_align = "-" + sequence2_align #add gap to sequence 2 alignment
		row -= 1 #move one up 
#print(sequence1_align) #printing alignment for sequence 1
#print(sequence2_align) #printing alignment for sequence 2

#Exercise 1.5: write alignment, alignment score, and number of gaps to an output file specifed by user. 

alignment_score = F_matrix[len(sequence1), len(sequence2)] #saving alignment score- the value in the last position in the F_matrix 

gap_num_seq1 = 0 #initializing the gap number for sequence 1
gap_num_seq2 = 0 #intializing the gap number for sequence 2

for position in range(len(sequence1_align)): #across the length of the sequence1 alignment
	if sequence1_align[position] == '-': #if there is a gap in sequence1 alignment at that position
		gap_num_seq1 += 1 #add one to the gap counter
	position+=1 #increase position by one


for position in range(len(sequence2_align)): #across the length of the sequence1 alignment
	if sequence2_align[position] == '-': #if there is a gap in sequence1 alignment at that position
		gap_num_seq2 += 1 #add one to the gap counter
	position+=1 #increase position by one

#print(gap_num_seq1) #printing gap number for sequence 1 to check. 
#print(gap_num_seq2) #printing gap number for sequence 1 to check. 


with open(file_name, 'w') as f: #outputting graph to a .txt format- user will provide file name in command line.
	f.write("Sequence 1 alignment \n") 
	f.write(sequence1_align) # adding sequence1 alignment
	f.write("\nSequence 2 alignment: \n") 
	f.write(sequence2_align) #adding sequence2 alignment
	f.write("\nThis number of gaps in the first sequence is:\n")
	f.write(str(gap_num_seq1)) #Adding gap number
	f.write("\nThis number of gaps in the second sequence is:\n")
	f.write(str(gap_num_seq2)) #Adding gap number
	f.write("\nThe score of this alignment is: \n") 
	f.write(str(alignment_score)) #adding in alignment score





 
