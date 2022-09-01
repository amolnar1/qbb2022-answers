#!/usr/bin/env python

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

x2 = [2, 4, 6]
y2 = [8, 64, 216]

##create a figure and axes
fig, ax = plt.subplots(nrows = 2)
#print(type(ax))
ax[0].plot(x, y, label = "x^2")
ax[1].plot(x2, y2, label = "X^3")
ax[0].legend()
ax[1].legend()
#plt.show()
##just shows the file doesn't save it
plt.savefig("lineplot.png")
##to save figure need argument of file name u want to save it to
plt.close(fig)