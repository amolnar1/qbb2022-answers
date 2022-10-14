#!/usr/bin/env python

import sys
import matplotlib.pyplot as plt
import math
import numpy as np
from bdg_loader import load_data

##bdg loader does it for parsing so we can graph
##need to run it with the cropped file


D0_H3K27ac_data = load_data(sys.argv[1])
##run with D0_H3K27ac_cropped.bdg


fig, axs = plt.subplots(4)
axs[0].bar(D0_H3K27ac_data['X'], D0_H3K27ac_data['Y'], width = 100)
axs[0].set_ylabel("H3K27ac Day 0")


D2_H3K27ac_data = load_data(sys.argv[2])
##run with D2_H3K27ac_cropped.bdg

axs[1].bar(D2_H3K27ac_data['X'], D2_H3K27ac_data['Y'], width = 100)
axs[1].set_ylabel("H3K27ac Day 2")

D2_Klf4_data = load_data(sys.argv[3])
##run with D2_Klf4_cropped.bdg


axs[2].bar(D2_Klf4_data['X'], D2_Klf4_data['Y'], width = 100)
axs[2].set_ylabel("Klf4 Day 2")


NA_treat_data = load_data(sys.argv[4])
##run with NA_treat_cropped.bdg


axs[3].bar(NA_treat_data['X'], NA_treat_data['Y'], width = 100)
axs[3].set_ylabel("Narrow Peaks")
plt.tight_layout()
plt.show()
plt.savefig("Figure6_homework5")


