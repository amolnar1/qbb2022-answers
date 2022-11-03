###################################
week 7

pt 1.

medaka_variant -i methylation.bam -f hg38.fa -r "chr11:1900000-2800000" -o chr11 -p 

medaka_variant -i methylation.bam -f hg38.fa -r "chr14:100700000-100990000" -o chr14 -p 

medaka_variant -i methylation.bam -f hg38.fa -r "chr15:23600000-25900000" -o chr15 -p 

medaka_variant -i methylation.bam -f hg38.fa -r "chr20:58800000-58912000" -o chr20 -p 

these are the regions:
chr11   1900000 2800000
chr14   100700000       100990000
chr15   1900000       25900000
chr20   58800000        58912000

pt 2. 

whatshap haplotag -o chr11_haplotag.bam --reference hg38.fa --regions chr11:1900000:2800000  --output-haplotag-list chr11_haplotypes.tsv round_0_hap_mixed_phased.vcf.gz methylation.bam	

cp ~/qbb2022-answers/week7/hg38.fa .

whatshap haplotag -o chr14_haplotag.bam --reference hg38.fa --regions chr14:100700000:100990000 --output-haplotag-list chr14_haplotypes.tsv round_0_hap_mixed_phased.vcf.gz methylation.bam

whatshap haplotag -o chr15_haplotag.bam --reference hg38.fa --regions chr15:23600000:25900000 --output-haplotag-list chr15_haplotypes.tsv round_0_hap_mixed_phased.vcf.gz methylation.bam

whatshap haplotag -o chr20_haplotag.bam --reference hg38.fa --regions chr20:58800000:58912000 --output-haplotag-list chr20_haplotypes.tsv round_0_hap_mixed_phased.vcf.gz methylation.bam

pt 3.

whatshap split --output-h1 chr20_type1.bam --output-h2 chr20_type2.bam chr20_haplotag.bam chr20_haplotypes.tsv

whatshap split --output-h1 chr15_type1.bam --output-h2 chr15_type2.bam chr15_haplotag.bam chr15_haplotypes.tsv

whatshap split --output-h1 chr14_type1.bam --output-h2 chr14_type2.bam chr14_haplotag.bam chr14_haplotypes.tsv

whatshap split --output-h1 chr11_type1.bam --output-h2 chr11_type2.bam chr11_haplotag.bam chr11_haplotypes.tsv

samtools cat chr20/chr20_type1.bam chr15/chr15_type1.bam chr14/chr14_type1.bam chr11/chr11_type1.bam -o type1.bam

samtools cat chr20/chr20_type2.bam chr15/chr15_type2.bam chr14/chr14_type2.bam chr11/chr11_type2.bam -o type1.bam

samtools view chr20_type1.bam to make sure it has stuff

pt 4.
samtools index type2.bam 
samtools index type1.bam 
to index for igv

Everything from type1 should be from one parent and everything from type2 should be from 
a different parent. This is because there is different methylation of the same genes, resulting
in different expression patterns. Methylation can be pased down to offspring, so the offspring
would get the methylation patterns from their respective parents. The difference in methylation
patterns indicates that type2 and type2 are from two different parents. 




