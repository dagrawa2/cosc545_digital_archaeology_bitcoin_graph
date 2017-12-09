from __future__ import division
import numpy as np
import pandas as pd
import scipy.stats as ss

dates = pd.read_csv("Graph_data\\attributes.csv")
dates = dates.as_matrix()
dates = dates[:,:3]
times = dates.dot(np.array([1,1/12,1/365]))
times = list(times)
order = ss.rankdata(times)
order = [int(i) for i in order]

file = open("Graph_data\\attributes.csv", "r")
lines = file.readlines()
lines = [line for line in lines if len(line) > 0]

file = open("Graph_data\\sorted.csv", "w")
file.write("time,"+lines[0])
for i in range(len(order)):
	file.write(str(i)+","+lines[order.index(i+1)+1])
file.close()