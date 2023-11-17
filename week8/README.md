To run Chicago:


Exercise 1.1:

Rscript runChicago.R /Users/cmdb/qbb2023-answers/week8/pchic_data/raw/PCHIC_Data/GM_rep1.chinput,/Users/cmdb/qbb2023-answers/week8/pchic_data/raw/PCHIC_Data/GM_rep2.chinput,/Users/cmdb/qbb2023-answers/week8/pchic_data/raw/PCHIC_Data/GM_rep3.chinput chicago_result --design-dir /Users/cmdb/qbb2023-answers/week8/pchic_data/raw/Design  --en-feat-list /Users/cmdb/qbb2023-answers/week8/pchic_data/raw/Features/featuresGM.txt -e washU_text

Exercise 1.2: 

Many of these enrichements make sense, as they are indicative of open chromatin regions, which would be more likely to be captured in pCHIC, as these are regions interacting with open promoter regions. For example, H3K4me1 and H3K27ac are both associated with open chromatin, and both have significant increases relative to random samples. Other marks are associated with facultative heterochromatin samples, and may indicate promoters and surrounding regions where expression is suppressed- for example, H3K4me3. However, other markers for facultative heterochromatin, such as H3K27me3, are not increased relative to random sampling.

In addition a few of these enrichements do not make sense, as they would not be predicted to interact with promoter regions. For example, both CTCF and H3K9me3 are upregulated- CTCF is indicative of TAD boundary regions, while H3K9me3 indicative constitutive heterochromatin such as telomeric and centromeric regions. Since no gene expression is expected at these regions, the enrichment of these features is unexpected. 


Exercise 2.2:

Promoter-promoter interactions: 

      chrom chromStart  chromEnd name score  value ex` color  ... sourceEnd      sourceName sourceStrand targetChrom targetStart targetEnd targetName targetStrand
2819  chr21   26837918  26939577    .   977  34.02   .     0  ...  26842640          snoU13            +       chr21    26926437  26939577   MIR155HG            +
1645  chr20   44438565  44565593    .   977  34.77   .     0  ...  44565593           PCIF1            +       chr20    44438565  44442365      UBE2C            +
1655  chr20   44438565  44607204    .   977  34.29   .     0  ...  44607204    FTLP1;ZNF335            +       chr20    44438565  44442365      UBE2C            +
3655  chr21   44582195  44849168    .   949  33.59   .     0  ...  44584504     AP001631.10            +       chr21    44845321  44849168       SIK1            +
3264  chr21   34849204  34868437    .   949   33.1   .     0  ...  34854619  RPS5P3;TMEM50B            +       chr21    34861480  34868437    DNAJC28            +
475   chr20   17660712  17951709    .   949  33.85   .     0  ...  17951709      MGME1;SNX5            +       chr20    17660712  17672229      RRBP1            +

Promoter-enhancer interactions: 

      chrom chromStart  chromEnd name score  value ex` color  ... sourceEnd          sourceName sourceStrand targetChrom targetStart targetEnd targetName targetStrand
2842  chr21   26797667  26939577    .   949  33.13   .     0  ...  26939577            MIR155HG            +       chr21    26797667  26799364          .            -
2254  chr20   55957140  56074932    .   920  32.29   .     0  ...  55973022  RBM38;RP4-800J21.3            +       chr20    56067414  56074932          .            -
2838  chr21   26790966  26939577    .   834  29.17   .     0  ...  26939577            MIR155HG            +       chr21    26790966  26793953          .            -
231   chr20    5585992   5628028    .   805  28.88   .     0  ...   5601172              GPCPD1            +       chr20     5625693   5628028          .            -
278   chr20    5515866   5933156    .   747  26.08   .     0  ...   5933156          MCM8;TRMT6            +       chr20     5515866   5523933          .            -
2839  chr21   26793954  26939577    .   747  26.23   .     0  ...  26939577            MIR155HG            +       chr21    26793954  26795680          .            -


Exercise 2.3:

MIR155HG:
MIR155HG is highly expressed in lymph nodes, so enhancer-promoter interactions are expected in B-cells such as GM12878 as expression is predicted to be high. Given how highly expressed it is in lymph tissue, it is no surprise that MIR155HG has three of the highest scores in the sample. 

GPCPD1: 
GPCPD1 is ubiquitously expressed in most tissues including the lymph nodes, indicating that it would be expected to be interacting with enhancers in GM12878 and expressing the GPCPD1 product. 