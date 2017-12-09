from __future__ import division
import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd

filenames = os.listdir("Flow_distros")

for filename in filenames:
	print "Plotting Flow_distros/"+filename+" . . . "
	date = filename[:-4]
	data = pd.read_csv("Flow_distros\\"+filename)
	data = data.as_matrix()
	x = data[:,0]
	y = data[:,1]

#	x = x[x<=50]
#	y = y[:x.shape[0]]

	fig = plt.figure()
	ax = fig.add_subplot(1,1,1)
	ax.plot(x, y, marker="o", markeredgecolor="none")
	ax.set_xlabel("Distance")
	ax.set_ylabel("Flow")
	ax.set_title("Bitcoin Flow over Distance ("+date+")")
	ax.set_yscale("log")
	fig.savefig("Plots\\Flow_distros\\"+date+".png", bbox_inches='tight')
	#plt.show()
