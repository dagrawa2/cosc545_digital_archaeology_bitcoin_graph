# Using python 2.7
import graph_tools as gt
import numpy as np
import time

time_0 = time.time()

# initialize transaction graph object
print "initializing graph . . . "
G = gt.tx_graph()

# build graph from CSV data
print "building graph . . . "
G.read_data("bigger_data.csv")

time_1 = time.time()
print "took ", np.round(time_1-time_0, 3), " seconds"

# save graph object to disk
print "pickling graph . . . "
gt.save(G, "bigger_graph")

time_2 = time.time()
print "took ", np.round(time_2-time_1, 3), " seconds"
