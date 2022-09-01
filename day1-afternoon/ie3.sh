##usage: ie3.sh input_vcf_fille nucleotide_of_interest

grep -v "#" $1 | awk '{if ($4 == "C") {print $5}}' | sort | uniq -c
## run this in command line
bash ie3.sh ~/data/vcf_files/random_snippet.vcf 
 484 A
 384 G
2113 T
## 1$ is so that we can put in any file and find the number of A,G,T when C is reference allele

#USAGE: ie3.sh input_vcf_file nucleotide_of_interest

nucoi=$2
grep -v "#" $1 | awk '{if ($4 == $nucoi) {print $5}}' | sort | uniq -c