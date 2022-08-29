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

cut -f 4 chromHMM.E116_15_coreMarks_hg38lift_stateno.chr21.bed | sort | uniq -c

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

c. to determine which fraction comprises the largest fraction of the genome, we would need to make a 5th column in the file determining how many basepairs comprise the region of interrest (subtrating the start from the stop column). Next, we would need to sort by regions 1-15 and then count how many basepairs total are in our new 5th column per region. Whichever has the most basepairs is the largest. We could also sort by size of the 5th column, whichever section has the most basepairs, that corresponding gene region would contain the largest fraction of the genome. 