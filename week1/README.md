Exercise 2.2:

1. For every year older that the mother is, there is an average increase of 0.3776 maternally-inherited de novo mutations. This was also observed in the generated graph, ex2_a.png. In the plot, there is a roughly positive linear trend in the data, but the slope of the line appears to be small (less than 0.5 by eye).

2. This relationship is significant, as the p-value is 6.888e-24. Because the p-value is so small, this suggests that the probability of obtaining these results under the null hypothesis (that there is no relationship) is so miniscule that there is likely a significant relationship. 

Exercise 2.3:

1. For every year older that the father is, there is an average increase of 1.3538 paternally-inherited de novo mutations. This is observed in the generated graph, ex2_b.png. While the plot for maternal age vs maternally-inherited de novo mutations had only a roughly positive linear trend with significant variation in number of mutations, the graph for paternally inherited de novo mutations vs father age has a much more clearly linear trend, with less variation in the data and a more agressive slope. As such, it makes sense that the number of inherited mutations would increase more rapidly with paternal age relative to maternal age. 
2. Because the p-value is very small, 1.55e-84, this relationship is significant.


Exercise 2.4:

B0 = 10.3263 (paternally inherited de-novo mutations) 
B1 = 1.3538 (paternally inherited de=novo mutations/year)
x = 50.5 years

y = B0 + x * B1
y = 10.3263 mutations + 50.5 years * 1.3538 mutations/year 
y = 78.9053 mutations

A proband is predicted to have 78.9053 paternally-inherited de novo mutations if they were born to a father who was 50.5 years of age at the time of their birth. 

Exercise 2.6:

1. I chose a t test in order to analyze if there was a significant difference in the mean number of mutations between the two groups (number of paternally inherited vs maternally inherited de novo mutations). If there is a significant difference between the mean of the groups, it follows that there is an overall signifcant difference between the groups.m 

2. Yes, there is a significant difference between the number of maternally vs paternally inherited de novo mutations. The t-test computes that the mean of paternally inherited de novo mutations is 53.4 mutations greater than the mean for the maternally inherited de novo mutations. In addition, the p-value is very small at 2.19e-264, indicating statistical significance.
