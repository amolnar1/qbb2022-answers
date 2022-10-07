lweek 4 hw


##we first need to make our file recognizable
VCF=~/vcf/genotypes.vcf
##making sure plink will recgonize the vcf file

plink --vcf genotypes.vcf --pca 10 --out week4pca 
##opening plink and telling it our vcf file
##next we run pca and ask for 10 values
##we then output this into a file named week4pca

This is the output:

week4pca.log
week4pca.eigenval	week4pca.nosex
week4pca.eigenvec

we get the allele frequencies:
plink --vcf genotypes.vcf -pca 10 --freq

4.
plink --vcf genotypes.vcf --pheno CB1908_IC50.txt --pca 10 --allow-no-sex --assoc --out week4
plink --vcf genotypes.vcf --pheno GS451_IC50.txt --pca 10 --allow-no-sex --assoc --out week4_GS


5. & 6. -- all the plotting stuff is in week4.py
need to run it ./week4.py genotypes.vcf

7. We are looking at the snp rs10876043 fromCB1908_IC50 phenotypes and rs1907642 from GS451_IC50 phenotypes
 in the UCSC genome browser. 
 
rs10876043: this is on gene DIP2B,  Disco-interacting protein 2 homolog B, which codes for a binding site 
for the transcriptional regulator DNA methyltransferase 1 associated protein 1 as well as AMP-binding sites.

rs1907642: This snp changes based on ethnic ancestry according to the browser. idk i cant find the name for it, 
in distress ya know

To figure out what this genome used is you could look at the header in the vcf