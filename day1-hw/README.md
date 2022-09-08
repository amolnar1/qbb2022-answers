## QBB2022 - Day 1 - Homework Exercises Submission
1. When we run the code: bash exercise1.sh ~/data/vcf_files/random_snippet.vcf
we get the error 'awk: illegale field $(), name "nuc"
I am assuming that this is letting us know that "nuc" is the wrong command to use.
We are trying to compare each nucleotide to the reference, cycling it through A, C, G, and T as the reference allele. It looks like it knows its supposed to cycle it through, but its unsure what 'nuc' means?
So the original awk did not recognize the variable 'nuc' because it was not defined within the awk script. it should look like:

for nuc in A C G T
do
  echo "Considering " $nuc
  awk -v awkvar="$nuc" '/^#/{next} {if ($4 == awkvar) {print $5}}' $1 | sort | uniq -c
done

in this we let awk know we have a variable with -v and then made sure that variable was defined in the $4 == X section

output:
Considering  A
 354 C
1315 G
 358 T
Considering  C
 484 A
 384 G
2113 T
Considering  G
2041 A
 405 C
 485 T
Considering  T
 358 A
1317 C
 386 G
 
 The corresponding nucleotide pairs (a:g/c:t) tend to have more mutations towards their corresponding partner. In terms of that basepair matching, it makes sense
 
 2. 
 The defining of the promoter region is very ambiguous and can contain many different options as defined in the 1-15 menomic description. I am including numbers 1,2,6,7,8,10 and 11 as potentially being involved in the promoter region. There is no defining of a strict promoter region and elements necessary for specific gene transcription.less
 
 Running the code:
 grep -Ew '1|2|6|7|8|10|11' chromHMM.E116_15_coreMarks_hg38lift_stateno.chr21.bed > promoterfile 
## this is to pull out any gene segment i believe may be involved in a promoter region and store it in a speciific file
## i than ran exercise2.sh that i made
promoterfile=/Users/cmdb/qbb2022-answers/day1-hw/promoterfile
echo $promoterfile
##set variable for vcffile
vcffile=/Users/cmdb/data/vcf_files/random_snippet.vcf
##using bedtools to compare genome overlap
bedtools intersect -a $vcffile -b $promoterfile > intersect_hw2.bed 
##these compare our vcffile to the promoter file and pull out only the vcfs that fall within the promoter region
## i than ran the previous exercise1.sh code with only C being specified to pull out only the C changes that occur within snps in the promoter region
for nuc in C 
do
  echo "Considering " $nuc
  awk -v awkvar="$nuc" '/^#/{next} {if ($4 == awkvar) {print $5}}' $1 | sort | uniq -c
done
results:
Considering  C
  36 A
  32 G
 149 T

 hypothesis/conclusions: Regardless of genomic area, when SNPs occur, 
 its more likely that the snp is a complementary basepair (a:g/c:t)
 
 3. 
 
 awk '/^#/{next} {print $1,$2-1, $2}' $1 > variants.bed
 ## its skipping anything starting with ## to make it more readable
 ## it is saying to print specific coordinates and put them in the file specified 
 sort -k1,1 -k2,2n ~/data/bed_files/genes.bed > genes.sorted.bed
 ## this is saying to sort specific fields (columns) and the -n denotes a numeric coding, this is then inputed into a bed file
 bedtools closest -a variants.bed -b genes.sorted.bed
 ## these files are then compared to one another
 
 the first error is that the file is not tab deliminated we can fix this by adding:
 
 awk -v OFS='\t' '/^#/{next} {print $1,$2-1, $2}' $1 

the second error is that both columns need numeric sorting, we can fix this by adding:
\sort -k1,1n -k2,2n > variants.sorted.bed
  
the final line of code is:
awk -v OFS='\t' '/^#/{next} {print $1,$2-1, $2}' $1 |  \sort -k1,1n -k2,2n > variants.sorted.bed

I dont know the sorting error message exactly, i had a bad file and originally could not get it to tab deliminate.
I knew there was a sorting error tho so i fixed that in the code before i realized my file was bad and could see the second error message.

To count variants, add | wc at the end of the last line of code
There are 10293 variants and 200 genes.
We can determine variants by just | wc for the bedtools output, giving 10293 lines or variants
We can then add | sort -u -k7,7 | to sort by column 7 for unique terms, which allows us to sort by uniqe gene name and then compile them
wc then allows us to get the count of lines, which becomes 200 after this 


  