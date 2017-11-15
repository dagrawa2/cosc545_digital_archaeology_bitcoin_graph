from __future__ import division
import numpy as np
import pandas as pd

data = pd.read_csv("flow.csv")
print "shape: ", data.shape

data = data.as_matrix()
print "np shape: ", data.shape

print "distance: ", np.mean(data[:,0]), " +- ", np.std(data[:,0])
print "flow: ", np.mean(data[:,1]), " +- ", np.std(data[:,1])
