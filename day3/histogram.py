#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np

#norm_data = np.random.normal(0, 1, int(1e6))
##simulates normally distributed random data
##numpy area with 50 points, mean of 0, stdev of 1

snp_af = np.genfromtxt("ALL_chr21_AF.txt")
##generating our data in from text
#print(snp_af.shape)

plt.hist(snp_af, bins = 50)

#plt.hist(norm_data, bins = 50vcf)

plt.show()