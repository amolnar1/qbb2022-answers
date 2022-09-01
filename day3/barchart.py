#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np

genes_per_chrom = np.genfromtxt("genes_per_chromsome.txt", dtype = None, 
encoding = None, names = ["gene_count", "chrom_name"])
fig, ax = plt.subplots()
ax.scatter(genes_per_chrom["chrom_name"], genes_per_chrom["gene_count"])

plt.show()

#print(genes_per_chrom["gene_count"])