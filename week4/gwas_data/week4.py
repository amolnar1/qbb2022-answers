#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np
import sys
from actualvcfParser import parse_vcf
##import the stuff

##########################################
##########################################

##this is the code to make the graph for 1v2

week4pca  = np.genfromtxt("week4pca.eigenvec", dtype = None, 
encoding = None, names = ["samp", "sample", "pca1", "pca2", "pca3", "pca4", "pca5", "pca6", "pca7", "pca8", "pca9", "pca10", "pca11", "pca12"])
##getting the file in and naming the different columns

fig, ax = plt.subplots()
ax.scatter(week4pca["pca1"], week4pca["pca2"])
##scatter the appropriate pca things that we pull from the file we genfromtext

ax.set_xlabel("PCA1")
ax.set_ylabel("PCA2")
ax.set_title("PCA 1 versus 2")
fig.savefig( "PCA1_2_scatter" + ".png" )
##save plot
#plt.show()

##########################################
##########################################
#
# ##now we need to figure out the allele frequency
#
# af_list = []
# gt00_list = []
# gt01_list = []
# gt11_list = []
# ##making the lists to put stuff in
#
# fname = sys.argv[1]
# ##getting file name from the command line
# vcf = parse_vcf(fname)
#
# #print(vcf[1])
# ##so the parsing is working
#
# for i in range(1, len(vcf)) :
#     snp = vcf[i]
#     #af_list.append(snp[7]["AF"])
#     gt00_count = 0
#     gt01_count = 0
#     gt11_count = 0
#     for j in range(9, len(snp)):
#         if (snp[j] == "0/0"):
#             gt00_count += 1
#         elif (snp[j] == "0/1" or snp[j] == "1/0"):
#             gt01_count += 1
#         elif (snp[j] == "1/1"):
#             gt11_count +=1
#     gt00_list.append(gt00_count / 256924)
#     gt01_list.append(gt01_count / 256924)
#     gt11_list.append(gt11_count / 256924)
# #print(gt00_list)
# ##she prints somethin ehhehe
# ##so now we have allele frequency i think

##i did it manually but then i learn plink ;)

##########################################
##########################################

##plotting this on histogram

fig, ax = plt.subplots()
allele_frequency  = np.genfromtxt("plink.frq", dtype = [int, str, str, str, float, int], encoding = None, 
names = ["CHR", "SNP", "A1", "A2", "MAF", "NCHROBS"])
##gen the stuff from text so we can get it from the rows ya know

#print(allele_frequency["MAF"])

plt.hist( (allele_frequency["MAF"]), density=True, bins = 10 )
ax.set_yscale('log')
ax.set_xlabel("Allele Frequency")
ax.set_ylabel("Density")
plt.show()
##make the histogram
##pull the histogram we pull the row "MAF" to get the things for it 

##########################################
##########################################

##oh no make manhattan plot

manhattan_GS  = np.genfromtxt("week4_GS.qassoc", dtype = [int, str, int, int, float, float, float, float, float], 
encoding = None, names = ["CHR", "SNP", "BP", "NMISS", "BETA", "SE", "R2", "T", "P"], skip_header = 1)
#
# fig, ax = plt.subplots()
# y = -np.log10(manhattan_GS["P"])
# x = range(len(y))
# ax.scatter(x, y)
# ax.legend()
# ax.set_xlabel("Genomic Location")
# ax.set_ylabel("-log 10 of P-val")
# plt.show()

pval = 0.00001
nosig = []
significant = []
x_nosig = []
x_significant = []
##to get the colors we want to divide all the things into different lists to plot against each other
##we make the different lists
##defining pval so we can use the variable

for i, thing in enumerate(manhattan_GS["P"]):
    ##for each thing we enumerate it and grab it from the row "P" in the thing
    if pval < thing: 
        ##only get pvals that are higher than our pval variable
        nosig.append(-np.log10(thing))
        ##we need it to be th -log10 for the stuff
        x_nosig.append(i)
        ##add to the thing
    else:
        significant.append(-np.log10(thing))
        x_significant.append(i)
        ##if not significant then we put it in here to plot
        ##we plot significant vs nonsignificant so that we can hae different colors

        

fig, ax = plt.subplots()

plt.scatter(x_nosig, nosig)
plt.scatter(x_significant, significant)
ax.legend()
ax.set_xlabel("Genomic Location")
ax.set_ylabel("-log 10 of P-val")
ax.set_title("GS451_IC50 Manhattan Plot")
plt.show()
##we scatter the stuff for the scatter plot 
##the nosig vs significant has the positions in it i think

manhattan_CB  = np.genfromtxt("week4.qassoc", dtype = [int, str, int, int, float, float, float, float, float], 
encoding = None, names = ["CHR", "SNP", "BP", "NMISS", "BETA", "SE", "R2", "T", "P"], skip_header =  1)
##gen from text the other pheotypes to do the same thing as above but with this phenotype


pval = 0.00001
nosig_2 = []
significant_2 = []
x_nosig_2 = []
x_significant_2 = []

for i, thing in enumerate(manhattan_CB["P"]):
    if pval < thing: 
        nosig_2.append(-np.log10(thing))
        x_nosig_2.append(i)
    else:
        significant_2.append(-np.log10(thing))
        x_significant_2.append(i)
        
fig, ax = plt.subplots()

plt.scatter(x_nosig_2, nosig_2)
plt.scatter(x_significant_2, significant_2)
ax.legend()
ax.set_xlabel("Genomic Location")
ax.set_ylabel("-log 10 of P-val")
ax.set_title("CB1908_IC50 Manhattan Plot")
plt.show()

###############################################################
###############################################################

#making a boxplot

highest_p = []
position_p = []
##need to make lists to put our different stuff to find it 

highest_p = (significant_2.index(max(significant_2)))
##gotta find the max of the significant and its position
##we put the position as the 10th value in that line
position_p = x_significant_2[10]
print(highest_p, position_p)
f = open("week4.qassoc")
##gotta open the right file we use this file to look for the gene name 

for i, line in enumerate(f): 
    ##go through and enumerate the line
    if i == position_p + 1 :
        ##adding 1 to the position because the first line is the header so we need to skip it 
        #print(line)
        line = line.strip().split()
        print(line[1])
        ##gotta get the stuff off the line
        ##line 1 will have the snp with the most signficiant pval for the specified phenotype
 
f = open("genotypes.vcf")  

##we are finding the lines with this phenotype
for line in f :
    if "rs10876043" in line :
        vcf_line = line
        vcf_line = vcf_line.strip().split()
        
##trying to find the stuff for the other thing
##this is the same as the stuff above but with the different phenotype

              
highest_p1 = []
position_p1 = []

highest_p1 = (significant.index(max(significant)))
position_p1 = x_significant[10]
print(highest_p1, position_p1)
f = open("week4_GS.qassoc")

for i, line in enumerate(f): 
    if i == position_p1 + 1 :
        #print(line)
        line = line.strip().split()
        print(line[1])

##we are making the lists to put the different 00, 01, 11 options in it

gt00_list = []
gt01_list = []
gt11_list = []

for i, item in enumerate(vcf_line) :
    ##going through the specified vcf line that we plled out above and counting the 00 01 and 11 stuff
    if item == "0/0" :
        gt00_list.append(i-8)
    elif item == "0/1" :
        gt01_list.append(i-8)
    elif item == "1/0" :
        gt01_list.append(i-8)
    elif item == "1/1" :
        gt11_list.append(i-8)
        ##adding the stuff to the appropriate list and -8 because there is 9 silly lines before it
        
#print(gt11_list)
#print(gt01_list)
##so there is stuff in both of these lists

phenotypes = open("CB1908_IC50.txt")
phen_00 =[]
phen_01 = []
phen_11 = []
##make lists for the stuff to go in

for i, line in enumerate(phenotypes) :
    ##enumerating the phenotypes so we know where they are and then looping through it
    if i in gt00_list :
        try:
            phen_00.append(float(line.strip().split()[2]))
        except:
            pass
            ##so for this part if i matches to something in the gen00 list then we put it in phen_00 to be graphed
            ##if its not in the 00 then it runs through everything for the 01 and 11
    elif i in gt01_list :
        try:
            phen_01.append(float(line.strip().split()[2]))
        except:
            pass
    elif i in gt11_list :
        try:
            phen_11.append(float(line.strip().split()[2]))
        except:
            pass

#print(phen_00)
        
 
box_plot = []

box_plot = [phen_00, phen_01, phen_11]
##we then plot the box plot

fig = plt.figure()
plt.boxplot(box_plot)
ax.set_xlabel("SNP Count")
ax.set_ylabel("Allele")
ax.set_title("CB1908_IC50 Box Plot")
plt.show()
    



        