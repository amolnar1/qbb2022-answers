## Feedback for day1-lunch from KW

### Exercise 2

* b (Mean): Good work

* c (Median): You can't directly find the median number given the files you have. It only has the genomic locations, not any info on which gene each exon belongs to. So gaking the `wc` of the exons file gives you a sum of the number of exons, but not a record of the number of exons for each gene. Since you just have location information, but no gene names, you want a different file which would have a fourth column recording which gene the exon is found in. Then you can keeping track of how many exons each gene has using `cut | sort | uniq -c`, sorting those counts, and finding the midpoint.

### Exercise 3

* b (Tally): Nice sort flag! Makes the output much more readable

* c (Fraction): And good reasoning on the largest fraction

### Exercise 4

* b (Tally): Very good

* c (All super populations): This is good reasoning for getting the info about the super populations as a whole. If you wanted to tally populations within the super populations though, you could run a similar command to b just 4 more times, switching out the super population each time, or you could do `cut -f2,3 integrated_call_samples.panel | sort | uniq -c | sort `

### Exercise 5

* b (HG00100.vcf): Good job making the file!

* c (genotypes): Very nice getting rid of the header!

* d (AF): Good work

* e (AFR_AF): Good reasoning

Estimated Completion: 100%
