
# Basic program to learn graph plots in python 

import numpy as np
import pylab as pl

x = [1, 2, 3, 4, 5, 6]
y = [1, 4, 9, 16, 25, 36]

x1 = [1,2,4,8,16,32,64]
y1 = [1,4,16,64,100,200,300]

# plot x and y 
pl.plot(x, y, 'r')
pl.plot(x1, y1, 'g')

"""
f1 = pl.figure(1)
pl.subplot(221)
pl.subplot(222)
pl.subplot(212)
"""

# setting axis limits
pl.xlim(0.0, 80.0)
pl.ylim(0.0, 380.0)

# axis titles 
pl.xlabel('x-axis')
pl.ylabel('y-axis')

# title of plot
pl.title('scatter plot')

# show it on screen 
pl.show()
