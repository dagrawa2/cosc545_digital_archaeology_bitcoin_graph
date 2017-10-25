# Using python 2.7
# May need to modify for python 3

import networkx as nx
import pandas as pd
import pickle

# Define a class for a graph
# whose nodes are bitcoin addresses and
# whose directed edges represent transaction values.
# This class inherits the methods of nx.DiGraph.

class addr_graph(nx.DiGraph):

	def __init__(self):
		nx.DiGraph.__init__(self)

	def read_data(self, filename):
		"""
		Builds graph from edge data recorded in "filename"
		"""
		# read data
		data = pd.read_csv(filename)
		# first column is input addresses
		inputs = list(data.iloc[:,0].values)
		# second column is output addresses
		outputs = list(data.iloc[:,1].values)
		# third column is transaction values
		values = list(data.iloc[:,2].values)
		# for every address appearing in the data
		for addr in list(set(inputs+outputs)):
			# add a node for each address
			self.add_node(addr)
		# for each line in the data
		for i in range(len(inputs)):
			# draw an edge between addresses weighted by value
			self.add_edge(inputs[i], outputs[i], value=int(values[i]))


# initialize graph and read in data
G = addr_graph()
G.read_data("data.csv")

# save graph object to disk
with open("graph.grph", "wb") as fp:
	pickle.dump(G, fp)