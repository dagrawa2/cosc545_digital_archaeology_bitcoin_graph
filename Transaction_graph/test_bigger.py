from __future__ import division
import networkx as nx
import graph_tools as gt
import time
import numpy as np

time_0 = time.time()

print "loading graph . . . \n"
G = gt.load("bigger_graph")

time_1 = time.time()
print "took ", np.round(time_1-time_0), " seconds\n"

print "order: ", G.order()
print "max in-degree: ", max(G.in_degree().values())
print "max out-degree: ", max(G.out_degree().values())
print "longest path length: ", nx.dag_longest_path_length(G)
print "number of components: ", nx.number_connected_components(G.to_undirected())
