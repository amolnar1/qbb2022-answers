#!/usr/bin/env python3

##we are going to have to run both random and db through the dictonary maker
##importing the vcfparser to use it 
from actualvcfParser import *
##makes a list of a list that we can use in python
kgp = parse_vcf("random_snippet.vcf")
dbsnp = parse_vcf("dbSNP_snippet.vcf")

##we want the key to be the chromsome & position and the value to be the ID
##key method one: (chromsome, position) (a touple)
##can also make key a string "chrom_pos" -> "chr21_235898570"
## dictonary set up: {("chr21", 218470329) : 'rs14u90823'}
##we want a dictonary to store dbSNP info
##we can then use chromsome and position to identify matches in random snippet

##read in the files 
                #fs=open("dbSNP_snippet.vcf","r")

dbsnp_dict={}
##making the dictonary to put in the stuff
##putting stuff into dictonary
##for every snp in dbsnp, we want to add that to the dictonary
for snp in dbsnp:
        chrom = snp[0]
        pos = snp[1]
        ##defining our stuff so we can add it to the dictonary
        newkey = (chrom, pos)
        newvalue = snp[2]
##adding snps and pos/chrom to the dictonary
        dbsnp_dict[newkey] = newvalue
        ##the dictonary is now made
        ##value is snp idea, key is chrom, pos as a touple 
#print(dbsnp_dict)
##just checking the dictonary was made and makes sense

##we now want to look up random snippet snps in the dbsnp dict. using chrom and position
##want to match snp to empty id in random snps

no_ID = 0
##making thing for coutner variable 

for snp in kgp:
    ##we want to get the snps positiion
    ##look for snp in dbsnp dict, need to create a query key (chr, pos)
    ##if snp is in dictonary, get its id
    ##report the number of random snippets without an id
    chrom = snp[0]
    pos = snp[1]
    query_key = (chrom, pos)
    ##too look up in dictonary, want to ask is our key in the dictonary
    ##if it is we can extract the associated value
    if query_key in dbsnp_dict:
        ##to extract value dict_name[key] will give value associated
        id_of_interest = dbsnp_dict[query_key]
        ##incrrement counter variable to store how many snps dont have an id 
    else :
        no_ID += 1 

print(no_ID)
##printing how many with no id 