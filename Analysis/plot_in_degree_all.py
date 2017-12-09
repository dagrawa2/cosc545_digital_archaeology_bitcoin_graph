from __future__ import division
import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd

filenames = os.listdir("In_degree_distros")

for filename in filenames:
	print "Plotting In_degree_distros/"+filename+" . . . "
	date = filename[:-4]
	data = pd.read_csv("In_degree_distros\\"+filename)
	data = data.as_matrix()
	x = data[:,0]
	y = data[:,1]

	x = x[x<=100]
	y = y[:x.shape[0]]

	fig = plt.figure()
	ax = fig.add_subplot(1,2,1)
	ax.plot(x, y)
	ax.set_xlabel("In-degree")
	ax.set_ylabel("Frequency")
	ax.set_title("In-Degree Distribution ("+date+")")
	ax.set_xscale("log")
	ax.set_yscale("log")
	fig.savefig("Plots\\In_degree_distros\\"+date+".png", bbox_inches='tight')
	#plt.show()
