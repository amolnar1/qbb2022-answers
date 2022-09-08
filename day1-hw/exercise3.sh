#!/bin/bash

#USAGE: bash exercise3.sh input_VCF

#awk '/^#/{next} {print $1,$2-1, $2}' $1 > variants.bed
awk '/^#/{next} {print $1,$2-1, $2}' $1 > variants.bed

#awk -v OFS='\t' '/^#/{next} {print $1, $2-1, $2}' variants.bed > deliminatedvariants.bed
#awk -v OFS='\t' '/^#/{next} {print $1, $2-1, $2}' random_snippet.vcf > deliminatedsnip.vcf

awk -v OFS='\t' '/^#/{next} {print $1,$2-1, $2}' $1 | sort -k1,1 -k2,2n > variants.sorted.bed

#sort -k1,1 -k2,2n ~/data/bed_files/genes.bed > genes.sorted.bed

#sort -k1,1n -k2,2n deliminatedvariants.bed > variants.sorted.bed
#sort -k1,1n -k2,2n deliminatedsnip.vcf > snip.sorted.bed

bedtools closest -a variants.bed -b genes.sorted.bed

#bedtools closest -a variants.sorted.bed -b snip.sorted.bed > 

