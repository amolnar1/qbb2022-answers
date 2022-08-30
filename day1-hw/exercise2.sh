promoterfile=/Users/cmdb/qbb2022-answers/day1-hw/promoterfile
echo $promoterfile
##set variable for vcffile
vcffile=/Users/cmdb/data/vcf_files/random_snippet.vcf
##using bedtools to compare genome overlap
bedtools intersect -a $vcffile -b $promoterfile > intersect_hw2.bed