#!/usr/bin/env python3

##we are going to have to run both random and db through the dictonary maker
##importing the vcfparser to use it 
from actualvcfParser import *
vcf = parse_vcf("random_snippet.vcf")

##we want the key to be the ID and the value to be the position

fs=open("dbSNP_snippet.vcf","r")
##opening the file into here
snpdict={}
##making the dictonary to put in the stuff
for line in fs:
    if line.startswith("#"):
        continue
    else:
        fields=line.strip().split('\t')
        fields[1]=int(fields[1])
        pos = fields[1]
        identification = fields[2]
        ##defining the fields for column 2 as an interger
        ##saying field 2 referrences position
        ##saying field 3 references the id 
        #snp[position]=identification

        snpdict[pos] = str(identification)
            
#key will be the ID
#value will be the POSITION    ​
#sanity check
for k, v in snpdict.items():
    print(k, v)
#for randSNP invv

#for pos in snp.keys():
 #   if pos = vcf[1][2]
  #  vcf[1][2] = identificaon
  
no_ID = 0

##vcf if our vcf random dictonary
##snpdict is our dbsnp dictonary
for i in range(1,len(vcf)) :
##we want to look at from skipping header through the length of the vcf file
##looking at random snps
   record = vcf[i]
   ##now going record by record through it
   pos = record[1]
   if pos in snpdict :
   ##mapping is dictonary for random snps, is position in dictonary
       ID = snpdict[pos]
       ##getting that value out of the dictonary
       for 
   else:
       no_ID += 1
print(no_ID)
       ##need to count how many do not have a dbsnp match