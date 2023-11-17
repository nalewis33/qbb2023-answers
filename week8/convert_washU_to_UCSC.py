#!/usr/bin/env python

import sys
import pandas as pd 

baitmap, washU, out = sys.argv[1:4] #user will supply the three input files- baitmap to be used, washU file to convert, and the output file name for the conversion. 



baits = pd.read_csv(baitmap,  delim_whitespace = True, names = ('CHR', 'Bait_Start', 'Bait_End', 'ID', 'GENE')) #reading in baitmap file as pandas df
#print(baits)

washU_csv = pd.read_csv(washU, sep= (",|\t"), names = ("CHR1", "Start_1", "End_1", "CHR2", "Start_2", "End_2", "Score"), engine = 'python') #reading in washU txt file as pandas df.
#print(washU_csv)



#Parsing out WashU data set based on figuring out which fragment is bait and which is target, also formatting into final dataset for UCSC format:

"""
1. chrom: The chromsome of the interaction
2. chromStart: The start position of the interaction (i.e. the start position of the lower of the two fragments) #minimum of starts
3. chromEnd: The end position of the interaction (i.e. the end position of the upper of the two fragments) #maximum of ends
4. name: You won't need this so you can just use a `.` to mark that it's missing
5. score: An integer score (0-1000) that describes the strength of the interaction. This is set to help with visualiztion. We'll describe below how to generate this.
6. value: The strength of the interaction
7. ex`: You won't need this so you can just use a `.` to mark that it's missing
8. color: Feel free to set a different color, but you can just use `0` to show the interactions in black
9. sourceChrom: The chromosome of the bait fragment
10. sourceStart: The start position of the bait fragment
11. sourceEnd: The end position of the bait fragment
12. sourceName: The name of the bait fragment (i.e. the name of the gene(s) for which the bait fragment is a marker)
13. sourceStrand: The "strand" of the bait fragment. You don't need this, but we recommend setting it to `+` to indicate that this is a bait fragment
14. targetChrom: The chromosome of the target fragment
15. targetStart: The start position of the target fragment
16. targetEnd: The end position of the target fragment
17. targetName: The name of the target fragment. If the target fragment is *also* a bait fragment, this should be the name of the fragment, otherwise you can mark it as empty with a `.`
18. targetStrand: The "strand" of the target fragment. Again, you don't need this, but we recommend setting it to `+` if the target is also a bait fragment, and `-` if it is not. It will help later on.
  
"""

UCSC_df = pd.DataFrame(columns=['chrom', 'chromStart', 'chromEnd', 'name', 'score', 'value', 'ex`', 'color', 'sourceChrom', 'sourceStart', 'sourceEnd', 'sourceName', 'sourceStrand', 'targetChrom', 'targetStart', 'targetEnd', 'targetName', 'targetStrand']) #generating dateframe with all needed info
max_strength = max(washU_csv["Score"]) #calculating max score, to be used to get strength
#print(max_strength)
#the mother of all for loops... 
for i in washU_csv.index: #for each value in washU_csv:
	UCSC_df.loc[i, 'chrom'] = washU_csv.loc[i, "CHR1"] #adding in chrom site
	UCSC_df.loc[i, 'chromStart'] = min(washU_csv.loc[i, "Start_1"], washU_csv.loc[i, "Start_2"])
	UCSC_df.loc[i, 'chromEnd'] = max(washU_csv.loc[i, "End_2"], washU_csv.loc[i, "End_1"])
	UCSC_df.loc[i, 'name'] = '.'
	UCSC_df.loc[i, 'score'] = int(int(washU_csv.loc[i, "Score"])/max_strength * 1000) #calculating score
	UCSC_df.loc[i, 'value'] = washU_csv.loc[i, 'Score']
	UCSC_df.loc[i, 'ex`'] = '.'
	UCSC_df.loc[i, 'color'] = '0'
	if washU_csv.loc[i, 'Start_1'] in baits['Bait_Start'].values: #If fragment 1 start is the same as a bait start (AKA it is the bait):
		j = int(baits[baits['Bait_Start'] == washU_csv.loc[i, 'Start_1']].index.values)
		#print(len(j))
		UCSC_df.loc[i, 'sourceChrom'] = washU_csv.loc[i, 'CHR1'] #source chromosome 
		UCSC_df.loc[i, 'sourceStart'] = washU_csv.loc[i, 'Start_1']
		UCSC_df.loc[i, 'sourceEnd'] = washU_csv.loc[i, 'End_1']
		UCSC_df.loc[i, 'sourceName'] = baits.loc[j , 'GENE']
		UCSC_df.loc[i, 'sourceStrand'] = '+'
		UCSC_df.loc[i, 'targetChrom'] = washU_csv.loc[i, 'CHR2']
		UCSC_df.loc[i, 'targetStart'] = washU_csv.loc[i, 'Start_2']
		UCSC_df.loc[i, 'targetEnd'] = washU_csv.loc[i, 'End_2']
		if UCSC_df.loc[i, 'targetStart'] in baits['Bait_Start'].values: #if fragment 2 is also a bait
			k = int(baits[baits['Bait_Start'] == washU_csv.loc[i, 'Start_2']].index.values)
			UCSC_df.loc[i, 'targetName'] = baits.loc[k , 'GENE'] #add in gene ID
			UCSC_df.loc[i, 'targetStrand'] = '+' #+ target
		else:
			UCSC_df.loc[i, 'targetName'] = "." #no gene id
			UCSC_df.loc[i, 'targetStrand'] = '-' #- target
	elif washU_csv.loc[i, 'Start_2'] in baits['Bait_Start'].values: #if fragment 2 is a bait start:
		j = int(baits[baits['Bait_Start'] == washU_csv.loc[i, 'Start_2']].index.values)
		UCSC_df.loc[i, 'sourceChrom'] = washU_csv.loc[i, 'CHR2']
		UCSC_df.loc[i, 'sourceStart'] = washU_csv.loc[i, 'Start_2']
		UCSC_df.loc[i, 'sourceEnd'] = washU_csv.loc[i, 'End_2']
		UCSC_df.loc[i, 'sourceName'] = baits.loc[j , 'GENE']
		UCSC_df.loc[i, 'sourceStrand'] = '+'
		UCSC_df.loc[i, 'targetChrom'] = washU_csv.loc[i, 'CHR1']
		UCSC_df.loc[i, 'targetStart'] = washU_csv.loc[i, 'Start_1']
		UCSC_df.loc[i, 'targetEnd'] = washU_csv.loc[i, 'End_1']
		if UCSC_df.loc[i, 'targetStart'] in baits['Bait_Start'].values: #if fragment 1 is a bait 
			k = int(baits[baits['Bait_Start'] == washU_csv.loc[i, 'Start_1']].index.values)
			UCSC_df.loc[i, 'targetName'] = baits.loc[k , 'GENE']
			UCSC_df.loc[i, 'targetStrand'] = '+' #+ target
		else: #if fragment 1 is not a bait
			UCSC_df.loc[i, 'targetName'] = "." #no gene ID
			UCSC_df.loc[i, 'targetStrand'] = '-' # - target


#print(UCSC_df)

with open(out, 'w') as f: #outputting graph to a .txt format- user will provide file name in command line.
	f.write('track type=interact name="pCHIC" description="Chromatin interactions" useScore=on maxHeightPixels=200:100:50 visibility=full \n') 
	UCSC_string = UCSC_df.to_string(header=False, index=False)
	f.write(UCSC_string)

#Exercise 2.2: 
"""
promoter_promoter = UCSC_df[UCSC_df['sourceStrand'] == UCSC_df['targetStrand']]
promoter_enhancer = UCSC_df[UCSC_df['sourceStrand'] != UCSC_df['targetStrand']]

promoter_promoter = promoter_promoter.sort_values(['score'], ascending = False)
promoter_enhancer = promoter_enhancer.sort_values(['score'], ascending = False)

print(promoter_promoter.head(6))
print(promoter_enhancer.head(6))
"""



