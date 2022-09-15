quant bio week 1
1.1 For 5x coverage: 50,000 (5x coverage x a million bp  / 100bp reads)
For 15x coverage : 150,000

1.2 The script is called genomessimulation.py

1.3 7,376bp was not covered. This matches the poisson expectations, 
which is outputted as 6.7379 x 10^3 (6,738)

1.4 6bp were not covered. This matches the poisson value that is outputted, which is fewer than 1.

2 de novo assembly
2.1 4 contigs

2.2 grep -v ">" contigs.fasta | wc
I used this to get the number of counts and lines without the fasta header.
Then its lines - words to get total contig count of 234467

2.3 using grep '>' contigs.fasta we can find the longest contig, which is 105830

2.4 The N50 is 47860

3.1 99.6972% average identity compared to the assembly.

dnadiff ~/qbb2022-answers/week1-answers/asm/asm/scaffolds.fasta ~/qbb2022-answers/week1-answers/asm/ref.fa

3.2 the out.report shows the longest alignment is 234497 

3.3 the out.report shows there is 1 insertion

4.1 the position of the insertion is 26788 - 27497

4.2 712 bp long

4.3 samtools faidx /path/to/genome.fa NODE_1_length_234497_cov_20.506978:26788-27497

insertion: >NODE_1_length_234497_cov_20.506978:26788-27497
ATACAATGCGTATTGTAGTATGGCCTTACGGGAGGGCAGACGGCAAAGAGTGATCACGTT
CTATCGGATGCAAGGCACCGCTTTATCCATTAGCCTCTTATTGGAGGAGGGCATGGCATT
CATACCCAATGGCTCAATTCTTTTACTACAACATTGATAACTTATCCAAGTACTCTACGA
CCAACCTGCAGAACGGCCCACCGGCCTAACGGCATACCTCACAACTACCCTGCTAAGGCG
AGCACTCCAGCCAAGCAAGACCACATCCACCCAAGCCCACCTCATCGCCTCAGCCAATAG
CGCTCAGACAAAAGGAACTTATTATTAACTGAAACGCTGTACTGCGGTAAGTCCTCAACG
CCGACCAAACGAAACCAGCAGCGTAGTCCTATCGGACTCGCTTGCACACATAACACATGC
TTGTAGTCTTGCACGACCCCAGGCGGACATGAGTTTCTGCTGGGCGGCGAGGAGTCGAAG
CTGCGGGCATTCCTTTCCGAAAACATGAATTACTGCGGGTATGTCCGACCTCAAACATTC
GTACCTGAGCATATTGCTCAAGTGAGCCAGTCGGCAATTCATATCCGAAAACATGACTGT
CTTGCATAAGGCCTCTCTTACGAGCTGAGTGCACGAACCACGGAACAGCTTAGTCACTTA
GAAGAGTACTCTATTCGGGACTTGAAGTACGCGTGCAATCGGGAACTAGT

4.4 ./dna-decode.py -d  --input asm/insertion

Congratulations to the 2022 CMDB @ JHU class!  Keep on looking for little green aliens..