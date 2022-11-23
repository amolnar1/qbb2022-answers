## Week 5 -- 10 points possible

1 + 0.5 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1  = 9.5 points out of 10

1. Filter reads, Call peaks, and intersect peaks across Sox2 replicates (0.33 points each)

* the genome size for mac2 callpeak should be different, [as seen here for chr17](https://github.com/igvteam/igv/blob/master/genomes/sizes/mm10.chrom.sizes)

2. Find the number of total peaks and overlapping peaks for Klf4 and Sox2 (0.5 for commands, 0.5 for result)

* For this, you've only looked at Sox2 peaks, but you want to see how many peaks overlap between Sox2 and Klf4, so something like
`bedtools intersect -a intersected_peaks.bed -b D2_Klf4_peaks.bed -wa > Sox2_Klf4_peaks.bed`. Then, find thet number of peaks for just Sox2 (intersected between replicates), just Klf4 (the `D2_Klf4_peaks.bed`), and then shared between Sox2 and Klf4. --> +0.5

3. scale bedgraph files (4 different datasets, 0.25 each)

4. crop bedgraph files (4 different datasets, 0.25 each)

5. python script for plotting


6. 4 panel plot of read pile ups

--> Didn't see the plot, but see the note in the readme for why it isn't there; +1

7. motif finding sort intersected sox2 replicate narrow peak by 5th columm, keep first 300 lines, awk command for reformatting (0.33 each)

8. use samtools faidx to extract peak sequences and meme-chip to perform motif finding (0.5 each)

9. download and unpack motif database

* code for having done this? I see that you have based off of the tomtom command; just please record such things

10. match profiles from tomtom for klf4 and sox2 (0.5 for commands, 0.5 for result)

* Nice way to grep multiple things at the same time! There should have been some SOX2 matches as well. Not sure why you don't see them
