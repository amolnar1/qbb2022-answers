#!/usr/bin/env python

import sys
import numpy as np
import matplotlib.pyplot as plt
from actualvcfParser import parse_vcf

af_list = []
gt00_list = []
gt01_list = []
gt11_list = []
##making the lists to put stuff in

fname = sys.argv[1]
##getting file name from the command line
vcf = parse_vcf(fname)

#print(vcf[1])

for i in range(1, len(vcf)) :
    snp = vcf[i]
    af_list.append(snp[7]["AF"])
    gt00_count = 0
    gt01_count = 0
    gt11_count = 0
    for j in range(9, len(snp)):
        if (snp[j] == "0|0"):
            gt00_count += 1
        elif (snp[j] == "0|1" or snp[j] == "1|0"):
            gt01_count += 1
        elif (snp[j] == "1|1"):
            gt11_count +=1 
    gt00_list.append(gt00_count / 2548)
    gt01_list.append(gt01_count / 2548)
    gt11_list.append(gt11_count / 2548)
#print(gt00_list)
 
##create a figure and axes
fig, ax = plt.subplots() # create a figure and axes
ax.scatter(af_list, gt00_list, label = "Hom. Ref. Freq.")
ax.scatter(af_list, gt01_list, label = "Het. Freq.")
ax.scatter(af_list, gt11_list, label = "Hom. Alt. Freq.")
ax.legend()
ax.set_xlabel("Allele frequency")
ax.set_ylabel("Genotype frequency")
plt.show()


parse_vcf()