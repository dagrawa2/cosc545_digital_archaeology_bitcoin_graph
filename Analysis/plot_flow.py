from __future__ import division
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = pd.read_csv("Flow_distros\\2017-11-15.csv")
data = data.as_matrix()
x = data[:,0]
y = data[:,1]

x = x[x<=50]
y = y[:x.shape[0]]

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.plot(x, y, marker="o", markeredgecolor="none")
ax.set_xlabel("Distance")
ax.set_ylabel("Flow")
ax.set_title("Bitcoin Flow over Distance")
ax.set_yscale("log")
fig.savefig("Plots\\2017-11-15_flow.png", bbox_inches='tight')
#plt.show()
