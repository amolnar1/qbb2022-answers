#!/usr/bin/env python3

import sys
import matplotlib.pyplot as plt
import math

vcf = sys.argv[1]
fs = open( vcf )

ac = []
for i, line in enumerate( fs ):
    if "#" in line:
        continue
    fields = line.split()
    info = fields[7].split(";")
    ac.append( int(info[0].replace("AC=","")))

fig, ax = plt.subplots()
ax.hist( (ac), density=True )
ax.set_yscale('log')
ax.set_xlabel("Allele Count")
ax.set_ylabel("Density")
ax.set_title("Allele Count Density")
fig.tight_layout()
fig.savefig( vcf + ".png" )

fs.close()

