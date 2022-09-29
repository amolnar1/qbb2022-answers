#!/usr/bin/env python3

import sys
import matplotlib.pyplot as plt
import math
import numpy as np

from actualvcfParser import parse_vcf

##import the stuff to use it

Parsed_vcf = parse_vcf("sCerrevisae_final.vcf")
##we already made a vcf parser so we use it 

#print(Parsed_vcf[1])

##pulling out allele frequency for first thing in Parsed_vcf
allele_frequency = []
predicted_effects = []
depth = []
quality = []
##we need dictonaries to put the stuff in that we pull out from the vcf file

for i in range(1,len(Parsed_vcf)) :
    ##looking through each thing after the header in the Parsed_vcf file (our scerreviase file after its been parsed)
    allele_frequency.append(Parsed_vcf[i][7]["AF"])
    ##the allele frequency is in the 7th thing in the list, and within that dictonary that makes up number 7 we want to pull out the value for AF
    annotation = Parsed_vcf[i][7]["ANN"]
##we wanted to pull out anythin the value for ANN in the 7th list item which is that same dictonary 
    predicted_effects.append(annotation.split('|')[1])
    ##we want to parse things by "|" (seperate everything by "|") we then want to take the 2nd value from that parsed list
    depth.append(Parsed_vcf[i][7]["DP"])
    ##we are looking for the the value for the key DP in list 7 which is a dictonary
    quality.append(Parsed_vcf[i][7]["QA"])
    ##looking for the value corresponding to key QA in list 7 which is a dictonary 
    
#print(quality)
    
#print(Parsed_vcf[i])
#print(predicted_effects)

effects = {}
##is i in effects already?

for i in predicted_effects :
    ##going through each thning in our predicted effects list
    if i in effects.keys() :
        effects[i] += 1
        ##if the effect is already in the dictonary, add +1 to the value interger for that key
    else: 
        effects[i] = 1
        ##if that key does not yet exist in the effects dictonary, add the key and make the value 1
        
#print(effects)
    


## we are now printing everything
##describe which plot we need, label x and y axis and give it a title

fig, axs = plt.subplots(2,2)
##this set up allows us to make the setup for the panel

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
##this makes the graph not look bad

plt.show()
##we then show the plot

