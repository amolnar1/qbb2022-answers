#!/bin/bash

#USAGE: bash exercise3.sh input_VCF

##so my file was bad, and i had a bunch of code that i tried before i realized was bad and deleted it so original code may be missing 

#awk '/^#/{next} {print $1,$2-1, $2}' $1 > variants.bed

awk -v OFS='\t' '/^#/{next} {print $1,$2-1, $2}' $1 > variants.bed
sort -k1,1 -k2,2n variants.bed > variants.sorted.bed
sort -k1,1 -k2,2n ~/data/bed_files/genes.bed > genes.sorted.bed


bedtools closest -a variants.sorted.bed -b genes.sorted.bed | wc
#| sort -u -k7,7 | wc
##this is to determine the number of genes