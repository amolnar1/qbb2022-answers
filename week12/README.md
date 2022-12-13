##readme for week 12

1B. 
python kronaconvert.py assembly.kraken SRR492186.kraken 
python kronaconvert.py assembly.kraken SRR492188.kraken 
python kronaconvert.py assembly.kraken SRR492189.kraken 
python kronaconvert.py assembly.kraken SRR492190.kraken 
python kronaconvert.py assembly.kraken SRR492193.kraken 
python kronaconvert.py assembly.kraken SRR492194.kraken 
python kronaconvert.py assembly.kraken SRR492197.kraken 
python kronaconvert.py assembly.kraken SRR492183.kraken

1C.
ktImportText -q SRR492183.kraken_krona.txt SRR492197.kraken_krona.txt 
SRR492194.kraken_krona.txt SRR492193.kraken_krona.txt
SRR492190.kraken_krona.txt SRR492188.kraken_krona.txt 
SRR492186.kraken_krona.txt SRR492189.kraken_krona.txt 

The majority of the bacteria are in the Terrabacteria group with 18% (the largest group) being
Finegoldia magna. Jack says nots enough bacteria.

2.
idk bro

2A. 
bwa index assembly.fasta 

2B.
bwa mem -t 

bwa mem -t 4 assembly.fasta ~/qbb2022-answers/week12/metagenomics_data/step0_givendata/READS/SRR492183_1.fastq ~/qbb2022-answers/week12/metagenomics_data/step0_givendata/READS/SRR492183_2.fastq > 183.sam
bwa mem -t 4 assembly.fasta ~/qbb2022-answers/week12/metagenomics_data/step0_givendata/READS/SRR492186_1.fastq ~/qbb2022-answers/week12/metagenomics_data/step0_givendata/READS/SRR492186_2.fastq > 186.sam
bwa mem -t 4 assembly.fasta ~/qbb2022-answers/week12/metagenomics_data/step0_givendata/READS/SRR492188_1.fastq ~/qbb2022-answers/week12/metagenomics_data/step0_givendata/READS/SRR492188_2.fastq > 188.sam
bwa mem -t 4 assembly.fasta ~/qbb2022-answers/week12/metagenomics_data/step0_givendata/READS/SRR492189_1.fastq ~/qbb2022-answers/week12/metagenomics_data/step0_givendata/READS/SRR492189_2.fastq > 189.sam
bwa mem -t 4 assembly.fasta ~/qbb2022-answers/week12/metagenomics_data/step0_givendata/READS/SRR492190_1.fastq ~/qbb2022-answers/week12/metagenomics_data/step0_givendata/READS/SRR492190_2.fastq > 190.sam
bwa mem -t 4 assembly.fasta ~/qbb2022-answers/week12/metagenomics_data/step0_givendata/READS/SRR492193_1.fastq ~/qbb2022-answers/week12/metagenomics_data/step0_givendata/READS/SRR492193_2.fastq > 193.sam
bwa mem -t 4 assembly.fasta ~/qbb2022-answers/week12/metagenomics_data/step0_givendata/READS/SRR492194_1.fastq ~/qbb2022-answers/week12/metagenomics_data/step0_givendata/READS/SRR492194_2.fastq > 194.sam
bwa mem -t 4 assembly.fasta ~/qbb2022-answers/week12/metagenomics_data/step0_givendata/READS/SRR492197_1.fastq ~/qbb2022-answers/week12/metagenomics_data/step0_givendata/READS/SRR492197_2.fastq > 197.sam

samtools sort 183.sam -o 183.bam
samtools sort 186.sam -o 186.bam
samtools sort 188.sam -o 188.bam
samtools sort 189.sam -o 189.bam
samtools sort 190.sam -o 190.bam
samtools sort 193.sam -o 193.bam
samtools sort 194.sam -o 194.bam
samtools sort 197.sam -o 197.bam

2D.
jgi_summarize_bam_contig_depths --outputDepth 183.txt 183.bam
jgi_summarize_bam_contig_depths --outputDepth 186.txt 186.bam
jgi_summarize_bam_contig_depths --outputDepth 188.txt 188.bam
jgi_summarize_bam_contig_depths --outputDepth 189.txt 189.bam
jgi_summarize_bam_contig_depths --outputDepth 190.txt 190.bam
jgi_summarize_bam_contig_depths --outputDepth 193.txt 193.bam
jgi_summarize_bam_contig_depths --outputDepth 194.txt 194.bam
jgi_summarize_bam_contig_depths --outputDepth 197.txt 197.bam

3A. 
metabat2 -i assembly.fasta -a 183.txt -o bins_dir/bin
4 bins
metabat2 -i assembly.fasta -a 186.txt -o bins_dir/bin
2 bins
metabat2 -i assembly.fasta -a 188.txt -o bins_dir/bin
3 bins
metabat2 -i assembly.fasta -a 189.txt -o bins_dir/bin
3 bins
metabat2 -i assembly.fasta -a 190.txt -o bins_dir/bin
2 bins
metabat2 -i assembly.fasta -a 193.txt -o bins_dir/bin
5 bins
metabat2 -i assembly.fasta -a 194.txt -o bins_dir/bin
3 bins
metabat2 -i assembly.fasta -a 197.txt -o bins_dir/bin
6 bins

There are 6 bins in total

3B.
grep ">" bin.*.fa | cut -d "_" -f 4 | paste -sd+ - | bc
11,965,344

grep -v ">" assembly.fasta | wc
38,708,237
This is about 31% of the assembly.

3C.
I think the bins look about right, the average size of a prokaryotic genome is 2-4Mb.
##each bin is thought to be the genome of one species in the gut 

3D.
You could align the bins to a library of different prokaryotic species.
If the bin is contaminated you would expect more than one prokaryote to align to the bin
and for there to be more ambiguity in which species it is.
To show its completelness, you can align it to the suspected species genome to observe how much
aligns to the full genome vs bin.

4. 

4A.
while read p; do grep p assembly.kraken; done < bin6 | cut -f 2 | sort | uniq -c | sort

bin6 predicted to be:
1050 root;cellular organisms;Bacteria;Terrabacteria group;Firmicutes;Tissierellia;Tissierellales;Peptoniphilaceae;Finegoldia;Finegoldia magna;Finegoldia magna ATCC 29328

bin5: 
5775 root;cellular organisms;Bacteria;Terrabacteria group;Firmicutes;Tissierellia;Tissierellales;Peptoniphilaceae;Finegoldia;Finegoldia magna;Finegoldia magna ATCC 29328

bin4:
1050 root;cellular organisms;Bacteria;Terrabacteria group;Firmicutes;Tissierellia;Tissierellales;Peptoniphilaceae;Finegoldia;Finegoldia magna;Finegoldia magna ATCC 29328

bin3:
it is probably contaminated; these two are close
7221 root;cellular organisms;Bacteria;Terrabacteria group;Firmicutes;Bacilli;Bacillales;Staphylococcaceae;Staphylococcus;Staphylococcus epidermidis;Staphylococcus epidermidis RP62A
7395 root;cellular organisms;Bacteria;Terrabacteria group;Firmicutes;Bacilli;Lactobacillales;Streptococcaceae;Streptococcus;Streptococcus pneumoniae

bin2:
9450 root;cellular organisms;Bacteria;Terrabacteria group;Firmicutes;Bacilli;Lactobacillales;Leuconostocaceae;Leuconostoc;Leuconostoc citreum;Leuconostoc citreum KM20

bin1:
3675 root;cellular organisms;Bacteria;Terrabacteria group;Firmicutes;Tissierellia;Tissierellales;Peptoniphilaceae;Finegoldia;Finegoldia magna;Finegoldia magna ATCC 29328

4B.
Running the metagenomic bin against a larger data set in a format similar to BLAST
would allow you to compare to many different genomes and also get a percent identity. 
Doing a comparison with a mathematical program such as a burrow-wheeler to compare the
similarity of top hits. s

