1. bwa index sacCer3.fa 

2. #bwa mem -R "@RG\tID:A01_09.fast\tSM:A01_09.fast" -t -o sacCer3.fa A01_09.fastq > A01_09.sam
#bwa mem -R "@RG\tID:A01_11.fastq\tSM:A01_11.fastq" -t -o sacCer3.fa A01_11.fastq > A01_11.sam
#bwa mem -R "@RG\tID:A01_23.fastq\tSM:A01_23.fastq" -t -o sacCer3.fa A01_23.fastq > A01_23.sam
#bwa mem -R "@RG\tID:A01_24.fastq\tSM:A01_24.fastq" -t -o sacCer3.fa A01_24.fastq > A01_24.sam
#bwa mem -R "@RG\tID:A01_27.fastq\tSM:A01_27.fastq" -t -o sacCer3.fa A01_27.fastq > A01_27.sam
#bwa mem -R "@RG\tID:A01_31.fastq\tSM:A01_31.fastq" -t -o sacCer3.fa A01_31.fastq > A01_31.sam
#bwa mem -R "@RG\tID:A01_35.fastq\tSM:A01_35.fastq" -t -o sacCer3.fa A01_35.fastq > A01_35.sam
#bwa mem -R "@RG\tID:A01_39.fastq\tSM:A01_39.fastq" -t -o sacCer3.fa A01_39.fastq > A01_39.sam
#bwa mem -R "@RG\tID:A01_62.fastq\tSM:A01_62.fastq" -t -o sacCer3.fa A01_62.fastq > A01_62.sam
#bwa mem -R "@RG\tID:A01_63.fastq\tSM:A01_63.fastq" -t -o sacCer3.fa A01_63.fastq > A01_63.sam

3a. 
#samtools sort -@4 -O bam -o A01_09.bam A01_09.sam
#samtools sort -@4 -O bam -o A01_11.bam A01_11.sam
#samtools sort -@4 -O bam -o A01_23.bam A01_23.sam
#samtools sort -@4 -O bam -o A01_24.bam A01_24.sam
#samtools sort -@4 -O bam -o A01_27.bam A01_27.sam
#samtools sort -@4 -O bam -o A01_31.bam A01_31.sam
#samtools sort -@4 -O bam -o A01_35.bam A01_35.sam
#samtools sort -@4 -O bam -o A01_39.bam A01_39.sam
#samtools sort -@4 -O bam -o A01_62.bam A01_62.sam
#samtools sort -@4 -O bam -o A01_63.bam A01_63.sam

3b. 
samtools index ${SAMPLE}.bam
samtools index A01_09.bam 
samtools index A01_11.bam 
samtools index A01_23.bam 
samtools index A01_24.bam 
samtools index A01_27.bam
samtools index A01_31.bam 
samtools index A01_35.bam 
samtools index A01_39.bam 
samtools index A01_62.bam 
samtools index A01_63.bam 

4. 
freebayes -f sacCer3.fa 
*.bam > sCerevisae.vcf

5. vcffilter -f "QUAL > 20" sCerevisae.vcf > sCerrevisae_filter.vcf

6. vcfallelicprimitives -k -g sCerrevisae_filter.vcf > sCerrevisae_alleles.vcf

7. snpeff ann R64-1-1.99 sCerrevisae_alleles.vcf > sCerrevisae_final.vcf

8. week3.py has all the code for making the graphs

week3.vcf has the first 1000 lines 

# A01_09.fastq
# A01_11.fastq
# A01_23.fastq
# A01_24.fastq
# A01_27.fastq
# A01_31.fastq
# A01_35.fastq
# A01_39.fastq
# A01_62.fastq
# A01_63.fastq
