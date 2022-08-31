# QBB2022 repository
 # QBB2022 - Day 1 - Lunch Exercises Submission

 1. I’m excited to learn genetics.

#question 2 answers
2. 13653 genes
to determine mean number of exons determine number of genes
wc genes.chr21.bed
yeilds 219 genes
wc exons.chr21.bed
yeilds 13653 exons
exon/gene = 1365/219 = 62.34 exons per gene

to determine the median, you must sort the exons file by the second column to put those that are the same next to each other and then count the ones that are similar using uniq and then sort them again to see which exon has the most occurances:
sort -k 2 exons.chr21.bed | uniq -c | sort
exons 41435836, 41437014, 41439693 all have 42 occurances 

3. determining which number of genome classified for each state
b. first i cut the 4th column of the file out which determines the state
i then sorted that so that each repeat would be enxt to each other
then we used uniqu -c to count how often these appeared

cut -f 4 chromHMM.E116_15_coreMarks_hg38lift_stateno.chr21.bed | sort -g | uniq -c

this is the output:
1- 305
2- 678
3- 79
4- 377
5- 808
6- 148
7- 1050
9- 654
10- 17
11- 17
12- 30
13- 62
14- 228
15- 678

c. to determine which fraction comprises the largest fraction of the genome, we would need to make a 5th column in the file determining how many basepairs comprise the region of interest (subtrating the start from the stop column). Next, we would need to sort by regions 1-15 and then count how many basepairs total are in our new 5th column per region. Whichever has the most basepairs is the largest. We could also sort by size of the 5th column, whichever section has the most basepairs, that corresponding gene region would contain the largest fraction of the genome. 

4. to determine the amount of individuals per super population:
b. we would search using grep for 'AFR', then cut out the 2nd column to only look at the sub populations within 'AFR', we would then sort these and then determine how many of each unnique subpopulation there are using uniq -c 

grep 'AFR' integrated_call_samples.panel | cut -f 2 |sort| uniq -c

results: 
 123 ACB
 112 ASW
 173 ESN
 180 GWD
 122 LWK
 128 MSL
 206 YRI

c. we cut out the 3rd column which had the super population data, then we sorted this data so all of the repeats would be next to each other. We then used uniq -c to count each uniq occurance
cut -f 3 integrated_call_samples.panel | sort | uniq -c 

results: 
1044 AFR
 535 AMR
 673 EAS
 670 EUR
 661 SAS
 
5. 
b. First we need to determien which columns we still need in our file which include 1-9 and 13 and then we will pipe this to our new file.
cut -f 1,2,3,4,5,6,7,8,9,13 random_snippet.vcf > HG00100.vcf 
c. To determine the values present for HG00100, we first want to remove the ## signs
grep -v # > HG00100.vcf
We will then take this output and select for only column 10 which is HG00100, sort this so like values are next to each other, and use uniq -c to count how often these occur 
cut -f 10 HG00100.vcf | sort |uniq -c
9514 0|0
 127 0|1
 178 1|0
 181 1|1
d. To determine the amount of rows contaning AF or allele frequency we want to specify for that desired AF and not the one denoting african countries. We did this through using ';AF' because allele freqency is deliminated with ';' we then pipped to wc to count the amount of AF=1.
grep ";AF=1." HG00100.vcf | wc
resultsS:
15
e. Depending on the dataset, it can appear more than once. AF can denote allele frequency and will always be in the vcf file. In this data set, AF denotes africa so it appears multiple times depending on where the sample is taken from
f. You would need to select for any line contaning 'AFR' and then pull out any value from 0-9 connected to the AFR_AF= statement. You could probably do this with awk.



 grep -Ew
 - E for multiple patterns, -w for exact match with pipes between it worked!!!!!
 