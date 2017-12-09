from __future__ import division
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = pd.read_csv("Comp_distros\\2017-11-15.csv")
data = data.as_matrix()
x = data[:,0]
y = data[:,1]

x = x[x<=100]
y = y[:x.shape[0]]

fig = plt.figure()
ax = fig.add_subplot(1,2,1)
ax.plot(x, y)
ax.set_xlabel("Out-degree")
ax.set_ylabel("Frequency")
ax.set_title("Component Size over Time")
ax.set_xscale("log")
ax.set_yscale("log")
fig.savefig("Plots\\2017-11-15_comp.png", bbox_inches='tight')
#plt.show()
