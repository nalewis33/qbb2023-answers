Exercise 1.1

1 Mbp * 3x Coverage = 3 Mbp

3 Mbp = 3,000,000 bp 

3000000 bp /100 bp/read = 30,000 reads


Exercise 1.3

1. About 50,000 bp, or roughly 5%, of the genome has not been sequenced at 3X coverage. 

2. This coverage better matches the coverage of the Poisson distribution as opposed to the normal distrubution. The coverage histogram is shifted leftward compared to the normal distribition, which more closesly aligns with the Poisson distribution. 

Exercise 1.4

1. In this simulation, there are less than 100 bp that have not been sequence at 10X coverage, or less than one hundreth of a percent of the total genome. 

2. At 10X coverage, the Poisson distribution matches the coverage of the reads well. In addition, unlike at 3X coverage where the histogram was shifted left relative to normal distribution, the normal distribution at 10X aligns well. 

Exercise 1.5

1. At 30X coverage, almost the entire genome is sequenced, with fewer than 10 bp (less than a thousandth of a percent) being missed.

2. At 30X coverage, both the Poisson distribution and normal distribution overlay the histogram of coverage nearly perfectly. At this level of coverage, the two distributions are near identical, as the Poisson distribution approaches the normal distribution as the coverage increases. 

Exercise 2.4:
To run in terminal:

conda activate graphviz 
cat Graph.txt | dot -Tpng > ex.2_digraph.png

Exercise 2.5

ATTCTTATTGATTCATTT

Exercise 2.6

In order to accurately reconstruct the genome, we would need to increase the lenght of each read, such as going from k=3 to k=4. With only three nucleotides per read, there is ambiguity introduced into the reads. For example, the read ATT and TTC both appear more than once. With this ambiguity, multiple different final sequences can be constructed. However, if the reads were increased to be larger, such as 4 nucleotides per read, this reduces the likelihood of ambiguous reads from occuring. 

Exercise 3.1:

Prompt input into ChatGPT: What makes genomics such an interesting field? Please cite references in your answer to justify its importance.

Answer provided by ChatGPT:

Genomics is an incredibly interesting and important field due to its profound impact on various aspects of science, medicine, and society. Here are some key reasons why genomics is so fascinating and important, along with references to justify its significance:

Unraveling the Blueprint of Life: Genomics provides a comprehensive understanding of the genetic material (DNA) that serves as the blueprint for all living organisms. This knowledge allows us to explore the genetic basis of life itself, uncovering the secrets of how organisms develop, function, and evolve. For example, the Human Genome Project, published in 2001, elucidated the complete human DNA sequence, revolutionizing our understanding of human biology (International Human Genome Sequencing Consortium, 2001).

Personalized Medicine: Genomics enables personalized medicine, tailoring medical treatments and therapies to an individual's unique genetic makeup. This approach has the potential to improve the effectiveness of treatments, minimize adverse effects, and enhance patient outcomes. For instance, genomics has been used to identify genetic markers associated with drug response variability (Relling et al., 2010).

Disease Understanding and Prevention: Genomics plays a pivotal role in the study of genetic diseases, helping identify causative mutations and mechanisms. It also aids in the development of genetic tests for disease risk assessment and early detection. Notable examples include the identification of BRCA1 and BRCA2 genes linked to breast cancer risk (Miki et al., 1994).

Evolutionary Insights: Genomics allows us to study the evolutionary history of species and populations. By comparing genomes across different organisms, we gain insights into the processes of speciation, adaptation, and genetic diversity. The study of ancient DNA has shed light on human evolution (Pääbo, 2014).

Biotechnology and Genetic Engineering: Genomics serves as the foundation for biotechnological advancements, including genetic engineering and synthetic biology. These technologies have revolutionized industries such as agriculture, medicine, and biofuel production. CRISPR-Cas9, a genome-editing tool, is a prominent example (Doudna and Charpentier, 2014).

Biodiversity Conservation: Genomics aids in the conservation of endangered species by helping to assess genetic diversity, identify subspecies, and design breeding programs for species at risk of extinction (Frankham, 2005).

Forensic Applications: Genomics has transformed forensic science, enabling DNA profiling and identification of individuals with high accuracy. This has had a profound impact on criminal investigations and justice (Butler, 2015).

Ethical and Societal Implications: The ethical, legal, and social implications (ELSI) of genomics raise thought-provoking questions about privacy, consent, discrimination, and more. Studying these issues is crucial to ensure responsible and equitable use of genomic information (McGuire et al., 2008).

In summary, genomics is an intriguing field because it has the power to unlock the secrets of life, transform healthcare, deepen our understanding of genetics and evolution, and address critical societal and ethical questions. It is a dynamic and multidisciplinary field with far-reaching implications for science and society.

References:

International Human Genome Sequencing Consortium. (2001). Initial sequencing and analysis of the human genome. Nature, 409(6822), 860-921.
Relling, M. V., & Evans, W. E. (2010). Pharmacogenomics in the clinic. Nature, 526(7573), 343-350.
Miki, Y., Swensen, J., Shattuck-Eidens, D., Futreal, P. A., Harshman, K., Tavtigian, S., ... & Ding, W. (1994). A strong candidate for the breast and ovarian cancer susceptibility gene BRCA1. Science, 266(5182), 66-71.
Pääbo, S. (2014). The human condition—a molecular approach. Cell, 157(1), 216-226.
Doudna, J. A., & Charpentier, E. (2014). The new frontier of genome engineering with CRISPR-Cas9. Science, 346(6213), 1258096.
Frankham, R. (2005). Genetics and extinction. Biological Conservation, 126(2), 131-140.
Butler, J. M. (2015). Forensic DNA typing: biology, technology, and genetics of STR markers (2nd ed.). Academic Press.
McGuire, A. L., Caulfield, T., Cho, M. K., & Research, N. I. H. G. E. (2008). Research ethics and the challenge of whole-genome sequencing. Nature Reviews Genetics, 9(2), 152-156.

Exercise 3.2:

While ChatGPT does a good job outlining basic points, there are several robotic phrases present throughout the essay. For example, the line "The ethical, legal, and social implications (ELSI) of genomics raise thought-provoking questions about privacy, consent, discrimination, and more" comes off as both stitled and generic, saying nothing meaningful and sounding like the hook to a 5-paragraph essay written by a high-schooler. Also, several of these citations have incorrect information in them. For examples, while there is a Relling et al. paper entitled "Pharmacogenomics in the clinc," it was published in 2015, not 2010 as ChatGPT cites. If ChatGPT were to actually go into details about the papers it cites, it likely would get facts in the paper wrong. Everything it cites, it only provides information that is obvious from the title or abstract, not the fine deatils. ChatGPT correctly cites the 1994 paper that identified BRAC1 and BRAC2 as a hereditary mutation that drastically increases an individual's risk for breast cancer, that information is given in the title, not in the minutiae of the paper itself. Overall, while the answer is mostly coherent and makes sense, it has a shallow depth of detail, contains awkward phrashing, and makes some mistakes in citing sources. 

