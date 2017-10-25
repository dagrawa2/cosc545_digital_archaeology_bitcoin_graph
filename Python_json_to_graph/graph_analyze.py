# Using python 2.7
# May need to modify for python 3

from graph_generate import addr_graph
import networkx as nx
import pandas as pd
import pickle

# read in saved graph object
with open("graph.grph", "rb") as fp:
	G = pickle.load(fp)

# print some graph attributes
print "order: ", G.order()
print "max in-degree: ", max(G.in_degree().values())
print "max out-degree: ", max(G.out_degree().values())