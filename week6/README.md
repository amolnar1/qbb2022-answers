##week 6 homework for quantbio

pt 1.

What percentage of reads are valid interactions (duplicates do not count as valid)?
31.3% for the dCTCF are valid interactions
30.8% for the ddCTCF are valid interactions

What constitutes the majority of invalid 3C pairs? What does it actually mean
 (you may need to dig into the HiC-Pro manual)?
 Dangling end pairs make up the majority of the invalid for dCTCF and ddCTCF. Dangling end pairs indicate
 a lower quality experiment with problems with digestion, fill in, or ligation steps.
 
 
 pt 2.
 
 # Were you able to see the highlighted difference from the original figure?
 yes i can see the highlighted differences from the original figure
 
 # What impact did sequencing depth have?
 a greater sequencing depth would give us more confidence about the signals we are currently seeing and 
 clarify any signals/interactions we may not be sure of. 

 # What does the highlighted signal indicate?
 things that have the highlighted signal have the highest interactions between each other.
 
 so for the full data we run it with this stuff:
 
./scriptweek6.py ddCTCF_full.6400.matrix dCTCF_full.6400.matrix 6400_bins.bed 
dCTCF_full.40000.matrix output


for the not full data we run it with thist stuff:

./scriptweek6.py ddCTCF_ontarget_6400_iced.matrix dCTCF_ontarget_6400_iced.matrix dCTCF_ontarget_6400_abs.bed dCTCF_full.40000.matrix output