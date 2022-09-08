# QBB2022 - day4 lunch assignment
##copied in the code from fred from the repo
##created the appropriate conda environment
##open -a Preview filename : opens the image
1.
a. this is the section of code specifying counting the bp in each vcf file:
  
  ##  echo "--- Subsetting $TYPE.vcf"
  ##bedtools sort -i $TYPE | bedtools merge | awk '{total+=$3-$2} END{print "    + Covering " total " bp"}'
  ##bedtools intersect -u -header -a $VCF -b $TYPE > $TYPE.vcf
##done
bp cout:

Subsetting exons.chr21.bed.vcf
    + Covering 1107407 bp
--- Subsetting processed_pseudogene.chr21.bed.vcf
    + Covering 956640 bp
--- Subsetting protein_coding.chr21.bed.vcf
    + Covering 13780687 bp
 
b. both of these files look the same. We can visually observe it and say that it looks the same
We could also write a python script that observes each data point and looks to see if there is a matching data point in the original file.
This would be done in a way similar to how we added ID's from dbSNPs to the random SNPs

- could also use cmp -b to make sure that the files are identical
- b flag to print out any differences
- can use bash function dif and md5sum

c. Three gene types that I am interested in are protein coding genes, lncRNA, and miRNA.
I really enjoy finding out the pathways and molecular interactions that come along with exploring protein coding genes.
I just enjoy the interplay between genetics and molecular interactions with them. lncRNA is interesting to me because it can often be overlooked. I may be working on an lncRNA project also.
miRNA is just interesting in all of the potentials it has in epigenetics and gene/protein interacttions. 

a. we added titles and log
b. we just needed to put "lncRNA" into the $TYPES list so it would also read that section
c. The data is right skewed for all plots. The higher the allele count for each data set, the lower the density of alleles.

3. adding documentation

SYNPOSIS: 
This script combines a gtf and vcf file by gene start and stop regions. The script allows for SNPs to be stored by gene type as identified in the gtf file.
The vcf file holds the information on allele count, and by combining these files we are able to see allele count and genetype for a given SNP all in one spot.
Finally, the script plots the allele count vs density for a given gene type, resulting in a graph of AC vs density for each gene type specified.

USAGE:
A random snippets file (or vcf file with SNPs) is needed to run this code against a gtf file, or gene trsansfer format file.

DEPENDANCIES:
Within our conda environment we need:
marplotlib version 3.5.1
bedtools version 2.30.0
python 3.10.4


DESCRIPTION:
in the github repository:
You first cd so that you can make a new directoy in which to run your code. 
The rest of the code then pulls the needed files from the github repo and opens them in the directory in a directory called cmdb-plots-vcf
The next section of code then creates a new conda environment in which to run the scripts in
finally we run the workflow (do_all.sh) with the needed files

do_all.sh is a script in which other scripts are specified to run.
Everything is first run throgh subset_regions.sh, which parses the gtf file according to gene type and outputs it into a bed file by gene type. 

After this, do_all.sh then takes the bed files and parses it further taking sections 2 and 3, and puts it into a vcf file matching up to the random_snippet vcf file.
This allows for the start and stop coordinates in the gtf file to be matched up with the start and stop coordinates in the vcf file.

This vcf file is then run through plot_vcf_ac.py.
This script gets rid of the headers and seperates each piece by ";" and plots the allele count as a histogram.
The allele count is then plotted against density, and each plot is saved as a png with a corresponding name. 

OUTPUT:
To get an example output, run the code found in bxlab/mdb-plot-vcfs README.md file
The output should be several histograms with "Density" on the y-axis and "Allele Count" on the x, The title should be "Allele Count Density"
