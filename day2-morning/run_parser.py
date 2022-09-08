#!/usr/bin/env python

import bed_parser
import statistics 

#read in random snippet vcf
bed = bed_parser.parse_bed("hg38_gencodev41_chr21.bed")

##find median number of exons for genes in bed file
##column 10 has the number of exons in it for that gene
##need to loop through every item of the list bed
##need to pull out column 10 for that item (count of exons in gene)
##when done with for loop, sort it from smallest to largest and find the middle most one
##create a list of all the number of exons per gene
##sort list, find middle value 

##can either download statistics and use median function (may need to conda install)
##or can pull out middle item of list 100 values mylist[49]
##mylist[len(mylist) / 2] 

number_of_exons = []
##making the list 

for i in range(len(bed)) :
    number_of_exons.append(bed[i][9])
##putting the exon numbers into the list that we made
##specified it by saying hey its a number
    
number_of_exons.sort()
##sorted it 

print(statistics.median(number_of_exons))
##printing the median
##used statistics import to do median 