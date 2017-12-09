from __future__ import division
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

headers = ["time","year", "month", "day", "order", "minInDegree", "maxInDegree", "meanInDegree", "stdInDegree", "minOutDegree", "maxOutDegree", "meanOutDegree", "stdOutDegree", "minComp", "maxComp", "meanComp", "stdComp", "longestPathLength", "minFlow", "maxFlow", "meanFlow", "stdFlow"]

data = pd.read_csv("Graph_data\\sorted.csv")
data = data.as_matrix()

time = data[:,headers.index("time")]
months = ["M","J","J","A","S","O","N","D"]

fig = plt.figure()
ax = fig.add_subplot(1,2,1)
ax.plot(time, data[:,headers.index("order")], color="black")
ax.set_xticks(np.arange(len(time)))
ax.set_xticklabels(2*months+months[:-1])
ax.set_xlabel("Month")
ax.set_ylabel("Order")
ax.set_title("Order over 2015-2017")
fig.savefig("Plots\\order.png", bbox_inches='tight')
#plt.show()

fig = plt.figure()
ax = fig.add_subplot(1,2,1)
ax.plot(time, data[:,headers.index("meanInDegree")], color="black")
ax.plot(time, data[:,headers.index("meanInDegree")]+data[:,headers.index("stdInDegree")], color="black", linestyle="dashed")
ax.set_xticks(np.arange(len(time)))
ax.set_xticklabels(2*months+months[:-1])
ax.set_xlabel("Month")
ax.set_ylabel("In-Degree")
ax.set_title("In-Degree over 2015-2017")
fig.savefig("Plots\\in_degree.png", bbox_inches='tight')
#plt.show()

fig = plt.figure()
ax = fig.add_subplot(1,2,1)
ax.plot(time, data[:,headers.index("meanOutDegree")], color="black")
ax.plot(time, data[:,headers.index("meanOutDegree")]+data[:,headers.index("stdOutDegree")], color="black", linestyle="dashed")
ax.set_xticks(np.arange(len(time)))
ax.set_xticklabels(2*months+months[:-1])
ax.set_xlabel("Month")
ax.set_ylabel("Out-Degree")
ax.set_title("Out-Degree over 2015-2017")
fig.savefig("Plots\\out_degree.png", bbox_inches='tight')
#plt.show()

fig = plt.figure()
ax = fig.add_subplot(1,2,1)
ax.plot(time, data[:,headers.index("meanComp")], color="black")
ax.plot(time, data[:,headers.index("meanComp")]+data[:,headers.index("stdComp")], color="black", linestyle="dashed")
ax.set_xticks(np.arange(len(time)))
ax.set_xticklabels(2*months+months[:-1])
ax.set_xlabel("Month")
ax.set_ylabel("Component Size")
ax.set_title("Component Size over 2015-2017")
fig.savefig("Plots\\comp.png", bbox_inches='tight')
#plt.show()

fig = plt.figure()
ax = fig.add_subplot(1,2,1)
ax.plot(time, data[:,headers.index("meanFlow")], color="black")
ax.plot(time, data[:,headers.index("meanFlow")]+data[:,headers.index("stdFlow")], color="black", linestyle="dashed")
ax.set_xticks(np.arange(len(time)))
ax.set_xticklabels(2*months+months[:-1])
ax.set_xlabel("Month")
ax.set_ylabel("Flow")
ax.set_title("Bitcoin Flow over 2015-2017")
fig.savefig("Plots\\flow.png", bbox_inches='tight')
#plt.show()
