# QBB 2022 - Day 3 - HW Exerci# QBB 2022 - Day 3 - HW Exercises
## 1. 
VCF=~/vcf/cichlid_full_filtered_rename.vcf.gz
##making sure plink will recgonize the vcf file
plink --vcf ALL.chr21.shapeit2_integrated_v1a.GRCh38.20181129.phased.vcf.gz 
--allow-extra-chr --pca 3 --out hw3pca 
##opening plink and telling it our vcf file
##we then allow for more than 22 chromosomes
##next we run pca and ask for only 3 values
##we then output this into a file named hw3pcases

##2. There appears to be 3 set clustering for this comparison. This is showing certain individuals are much more closely related than other groups of individuals, so these individuals are more likely to be closer to one another geographically. 

##we are comparing allele frequency to population and seeing the variation and similarities between individduals

this is in day3hw.py 
code for pt 2:
##this is the code to make the graph for 1v2
hw3pca = np.genfromtxt("hw3pca.eigenvec", dtype = None, 
encoding = None, names = ["names1", "names2", "pca1", "pca2", "pca3"])
##getting the file in and naming the different columns

fig, ax = plt.subplots()
ax.scatter(hw3pca["pca1"], hw3pca["pca2"])

ax.set_xlabel("PCA1")
ax.set_ylabel("PCA2")

fig.savefig( "PCA1_2_scatter" + ".png" )
##save plot
plt.show()

##this is code for 1v3
hw3pca = np.genfromtxt("hw3pca.eigenvec", dtype = None, 
encoding = None, names = ["names1", "names2", "pca1", "pca2", "pca3"])
##getting the file in and naming the different columns

fig, ax = plt.subplots()
ax.scatter(hw3pca["pca1"], hw3pca["pca3"])

ax.set_xlabel("PCA1")
ax.set_ylabel("PCA3")

fig.savefig( "PCA1_3_scatter" + ".png" )
plt.show()

##3. here is the code I used for pt 3

#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np

##start superpop
fig, ax = plt.subplots()

join = np.genfromtxt("hw3joinoutput", dtype = None, 
encoding = None, names = ["names1", "names2", "pca1", "pca2", "pca3", 
"subpop", "superpop", "sex"])
##putting in our file from the command line and labeling each column

superpop = (np.unique(join["superpop"]))
##making a list of the unique items in the superpop column
for each in superpop:
    x = []
    y = []  
##for each in the superpop, record an x and y value  
    for thing in join:
        if each == thing[6]:
            x.append(thing[2])
            y.append(thing[3])
##for each thing (item) in join in column6 (superpop) append thing 2 & 3 (PCA1 & 2)
##this allows us to add a color 
    ax.scatter(x, y, label = each)
##scatter the x & y and label each thing (superpop)(this allows us to label it by color)
    ax.legend()
ax.set_xlabel("PCA1")
ax.set_ylabel("PCA2")
ax.set_title("PCA 1 versus 2 Determined by Superpopulation")

fig.savefig( "PCA1_2_superpop" + ".png" )
plt.show()
##we then add a legened, label axis, and label the graph
##this approach can be applied to subpop and gender by just changing the specifics to that corresponding column
##so just change the specifics but the coding structure stays the same 

##start subpop
fig, ax = plt.subplots()

join = np.genfromtxt("hw3joinoutput", dtype = None, 
encoding = None, names = ["names1", "names2", "pca1", "pca2", "pca3", 
"subpop", "superpop", "sex"])

subpop = (np.unique(join["subpop"]))
for each in subpop:
    x = []
    y = []    
    for thing in join:
        if each == thing[5]:
            x.append(thing[2])
            y.append(thing[3])
    ax.scatter(x, y, label = each)
    ax.legend()
ax.set_xlabel("PCA1")
ax.set_ylabel("PCA2")
ax.set_title("PCA 1 versus 2 Determined by Subpopulation")
fig.savefig( "PCA1_2_subpop" + ".png" )
plt.show() 

##start gender
fig, ax = plt.subplots()

join = np.genfromtxt("hw3joinoutput", dtype = None, 
encoding = None, names = ["names1", "names2", "pca1", "pca2", "pca3", 
"subpop", "superpop", "sex"])

sex = ("female", "male")
for each in sex:
    x = []
    y = []    
    for thing in join:
        if each == thing[7]:
            x.append(thing[2])
            y.append(thing[3])
    ax.scatter(x, y, label = each)
    ax.legend()
ax.set_xlabel("PCA1")
ax.set_ylabel("PCA2")
ax.set_title("PCA 1 versus 2 Determined by Gender")
fig.savefig( "PCA1_2_sex" + ".png" )
plt.show()     