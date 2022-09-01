##goal: Number of SNPs in the 1000 genomes file that intersect each gene and how many unique genes are represented
##setting variables
genefile=/Users/cmdb/data/bed_files/genes.bed
echo $genefile
##set variable for vcffile
vcffile=/Users/cmdb/data/vcf_files/random_snippet.vcf
##using bedtools to compare genome overlap
bedtools intersect -a $genefile -b $vcffile > intersect_out_ie2.bed
##pulling out overlap and putting into new file
wc intersec_out_ie2.bed
##number of snps that intersect one gene
## looking for number of unique genes
## cut out column 4 cause has genes
## sort by gene and then uniq to determine hoe many overlap
## wc so that we can count how many genes
cut -f 4 intersect_out_ie2.bed | sort |uniq -c | wc 
##answer is 166 unique genees

##whats the most common alternate allele for cytesine in ?idk
##this will give us our columns of interest 
grep "#" ~/data/vcf_files/random_snippet.vcf | tail -n 1 | cut -f 1,2,3,4,5
#CHROM	POS	ID	REF	ALT
##idk why we did this
grep -v "#" ~/data/vcf_files/random_snippet.vcf| cut -f 4 | sort |uniq -c
##2027 A
##2981 C
##2931 G
##2061 T

awk '{print $4}' ~/data/vcf_files/random_snippet.vcf | sort| uniq -c

   7 
2027 A
2981 C
2931 G
   1 REF
2061 T
   1 alleles
   1 alternate
   1 in
   1 of
   1 some
   5 the
   1 variant
   1 with
   
awk '/^#/{next} {print $4}' ~/data/vcf_files/random_snippet.vcf | sort| uniq -c
 ## ^ means to look at the begining of the line (does line start with #), {next} means skip it  2027 A
   2981 C
   2931 G
   2061 T
   
   grep -v "#" ~/data/vcf_files/random_snippet.vcf | awk '{if ($4 == "C") {print $5}}' | sort | uniq -c
    484 A
    384 G
   2113 T
## i have no idea what this means
##number of A,G, T when C is reference allele
##so common alternate allele when C is referrence is T
   