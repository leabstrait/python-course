# There are a few modules included in the matplotlib
# package, but we will only work with the basic plotting module, pyplot.

import tkinter
from matplotlib import pyplot as plt

# Hello matplotlib
from matplotlib import pyplot as plt
plt.plot([2,4,6,8,10])
plt.show()

# Use axis starting from 1
plt.plot([1,2,3,4,5], [2,4,6,8,10])
plt.show()

# Change plotted line styles

plt.plot([1,2,3,4,5], [2,4,6,8,10], "g-o")
plt.show()

# https://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.plot

# Generate numbers for the plot
from numpy import arange
plt.plot(arange(2,12,2), "g-o")
plt.show() # displays the same graph as the previous example

# To plot multiple sets of points, we add them to plot() as additional arguments:
 
from numpy import arange
xPoints = arange(1,21)
baseline = arange(0,20)
plt.plot(xPoints, baseline**2, "g-o", xPoints, baseline, "r-^")
# plt.axis([0, 21, 0, 400]) # Give the axes a litle room to breathe
plt.show()


# Add more information to the plots
xPoints = arange(1,21)
baseline = arange(0,20)
plt.plot(xPoints, baseline**2, "g-o", xPoints, baseline, "r-^")
plt.axis([0, 21, 0, 400])
plt.title("Amount of Python learned over time")
plt.xlabel("Days")
plt.ylabel("Standardized knowledge index score")
plt.legend(("By taking this course", "Otherwise"), loc=2)  # loc is location
plt.show()


# Bar Chart
plt.bar(arange(0,10), arange(1,21,2))
plt.show()

# Change bar width
plt.bar(arange(0,10), arange(1,21,2), width=.5)
plt.show()

# Histograms
from numpy import random
plt.hist(random.randn(10000), 20)
# histogram of 10,000 normally distributed (Gaussian) random numbers binned across 20 possible bars
plt.show()


# Courtesy ACEM BEX
x = range(-180,180)
plt.plot(list(x),list(map(math.sin, list(map(lambda t: t*math.pi/180,x)))))
plt.show()
