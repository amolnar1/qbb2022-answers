##week 5 homework

1. samtools view -b -q 10 D2_Sox2_R1_input.bam > D2_Sox2_R1_input_filtered.bam
samtools view -b -q 10 D2_Sox2_R2_input.bam > D2_Sox2_R2_input_filtered.bam
samtools view -b -q 10 D2_Sox2_R2.bam > D2_Sox2_R2.bam_filtered.bam
samtools view -b -q 10 D2_Sox2_R1.bam > D2_Sox2_R1_filtered.bam

2. 
macs2 callpeak -f BAM -t D2_Sox2_R2.bam_filtered.bam -c D2_Sox2_R2_input_filtered.bam -g 8.3e+7 -B --outdir D2_Sox2_R2
##need to out put it into something
macs2 callpeak -t D2_Sox2_R1_filtered.bam -c D2_Sox2_R1_input_filtered.bam -g 8.3e+7 -B --outdir D2_Sox2_R1


3. 
bedtools intersect -a D2_Sox2_R1/NA_peaks.narrowPeak -b D2_Sox2_R2/NA_peaks.narrowPeak > intersected_peaks.bed
##intersecting the technical replicates, need two replicates to get rid of the noise and to amke sure the peak is real

4. 
wc intersected_peaks.bed 
     582    5820   39793 intersected_peaks.bed

bedtools intersect -a D2_Sox2_R1/NA_peaks.narrowPeak -b D2_Sox2_R2/NA_peaks.narrowPeak -c | wc
	761    8371   53514
##to report the number of overlapping features
## there are 761 peaks, 582 which overlap
## 76.5% of peaks from Klf4 colocalize with Sox2

5. 
	1. 	# python scale_bdg.py D0_H3K27ac_treat.bdg D0_scaled.bdg
	# 	python scale_bdg.py D2_H3K27ac_treat.bdg D2_scaled.bdg
	##we dont need to run it for the ones above
		python scale_bdg.py D0_H3K27ac_treat.bdg D0_H3K27ac_scaled.bdg
		python scale_bdg.py D2_H3K27ac_treat.bdg D2_H3K27ac_scaled.bdg
		python scale_bdg.py D2_Klf4_treat.bdg D2_Klf4_scaled.bdg
		python scale_bdg.py NA_treat_pileup.bdg NA_treat_scaled.bdg
	##bins the reads into 100bp for plotting
	
	2. 
	# awk '{ if ($2 < 35507055 && $3 > 35502055) print $0 }' D0_scaled.bdg > D0_cropped.bdg
# 	awk '{ if ($2 < 35507055 && $3 > 35502055) print $0 }' D2_scaled.bdg > D2_cropped.bdg
	awk '{ if ($2 < 35507055 && $3 > 35502055) print $0 }' D0_H3K27ac_scaled.bdg > D0_H3K27ac_cropped.bdg
	awk '{ if ($2 < 35507055 && $3 > 35502055) print $0 }' D2_H3K27ac_scaled.bdg > 2_H3K27ac_cropped.bdg
	awk '{ if ($2 < 35507055 && $3 > 35502055) print $0 }' D2_Klf4_scaled.bdg > D2_Klf4_cropped.bdg
	awk '{ if ($2 < 35507055 && $3 > 35502055) print $0 }' NA_treat_scaled.bdg > NA_treat_scaled.bdg
	##awk pulls out regions of itnerest, genomic start and stop 
	
	4. ./figure6.py D0_H3K27ac_cropped.bdg D2_H3K27ac_cropped.bdg D2_Klf4_cropped.bdg NA_treat_cropped.bdg

pt 2.
	
1/2/3. sort -n -k5 NA_peaks.narrowPeak | head -300 | awk '{ printf "%s:%i-%i\n", $1, $2, $3 }' > sorted_NA_peaks.narrowPeak
##this file has the location of the peaks and in step 4 we want to get the sequences out

4. samtools faidx -r sorted_NA_peaks.narrowPeak mm10.fa > extracted_peals.fa

5. meme-chip  -maxw 7 -oc meme.chip.stuff extracted_peals.fa
##finding putative sox2 binding sites

part 3.

	2. tomtom -o mouse.tomtom.stuff combined.meme ~/Downloads/motif_databases/MOUSE/HOCOMOCOv11_full_MOUSE_mono_meme_format.meme
	##looking for other dsicovered TF binding sites
	##showing a lot of them are known KLF4 bidning sites

 	4. grep -e "KLF4" -e "SOX2" tomtom.tsv > klf4.sox2.tomtom
	##pulling out where this region has been previously identified and seeing it has been identified with KLF4 binding
	##showing that KLF4 and SOX2 could share binding sites
	
things to add to github:
klf4.sox2.tomtom
README.md
figure6.py
i would save my figure as a pdf but it is now saying matplotlib isn't a thing after I have already 
ran my script and gotten real graphs :(
also, my counts for the number of peaks are run as a command and not saved to a file, the number 
of peaks is commented under the command at the specific step

