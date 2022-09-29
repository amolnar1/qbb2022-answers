#!/usr/bin/env python3

import sys
import matplotlib.pyplot as plt
import math
import numpy as np

from actualvcfParser import parse_vcf

Parsed_vcf = parse_vcf("sCerrevisae_final.vcf")

#print(Parsed_vcf[1])

##pulling out allele frequency for first thing in Parsed_vcf
allele_frequency = []
predicted_effects = []
depth = []
quality = []

for i in range(1,len(Parsed_vcf)) :
    allele_frequency.append(Parsed_vcf[i][7]["AF"])
    annotation = Parsed_vcf[i][7]["ANN"]
    predicted_effects.append(annotation.split('|')[1])
    depth.append(Parsed_vcf[i][7]["DP"])
    quality.append(Parsed_vcf[i][7]["QA"])
    
#print(quality)
    
#print(Parsed_vcf[i])
#print(predicted_effects)

effects = {}
##is i in effects already?

for i in predicted_effects :
    if i in effects.keys() :
        effects[i] += 1
    else: 
        effects[i] = 1
        
#print(effects)
     
    



fig, axs = plt.subplots(2,2)

axs[0,0].hist( (allele_frequency), density=True )
axs[0,0].set_yscale('log')
axs[0,0].set_xlabel("Allele Frequency")
axs[0,0].set_ylabel("Density")
axs[0,0].set_title("Allele Frequency Density")
#fig.tight_layout()
    
#making bar chart
axs[0,1].bar(effects.keys(), effects.values())
axs[0,1].set_title('Predicted Effects')
axs[0,1].set_xlabel('variant type')
axs[0,1].set_ylabel('count')
#fig.tight_layout()


axs[1,0].hist( (quality), density=True )
axs[1,0].set_yscale('log')
axs[1,0].set_xlabel("Quality Distribution")
axs[1,0].set_ylabel("Density")
axs[1,0].set_title("Quality Dsitribution Density")
#fig.tight_layout()


axs[1,1].hist( (depth), density=True )
axs[1,1].set_yscale('log')
axs[1,1].set_xlabel("Read Depth")
axs[1,1].set_ylabel("Density")
axs[1,1].set_title("Read Depth Density")
#fig.tight_layout()

fig.tight_layout()
plt.show()


