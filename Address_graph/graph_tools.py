# Using python 2.7
import networkx as nx
import pandas as pd
import pickle

class addr_graph(nx.DiGraph):
	"""
	This class defines a directed graph object
	whose nodes represent unique bitcoin addresses and
	whose edges represent _expected_ transaction values.
	This class inherits from the nx.DiGraph class.
	"""
	
	def __init__(self):
		"""
		Initializes a graph object.
		"""
		nx.DiGraph.__init__(self)

	def read_data(self, filename):
		"""
		Builds graph from edge data recorded in filename.
		Args:
			filename (str): Filename of CSV data.
		"""
		# read data
		data = pd.read_csv(filename)
		# first column is input addresses
		inputs = list(data.iloc[:,0].values)
		# second column is output addresses
		outputs = list(data.iloc[:,1].values)
		# third column is transaction indeces
		indeces = list(data.iloc[:,2].values)
		# fourth column is expected transaction values
		values = list(data.iloc[:,3].values)
		# add a node for every address in the data
		for addr in list(set(inputs+outputs)):
			self.add_node(addr)
		# for each line in the data
		for i in range(len(inputs)):
			# draw an edge between addresses weighted by hash and value
			self.add_edge(inputs[i], outputs[i], tx_index=int(indeces[i]), value=float(values[i]))


def save(graph, filename):
	"""
	Pickles an addr_graph object to filename.
	Args:
		graph (addr_graph): Graph to be pickled.
		filename (str): Filename where graph will be written.
	"""
	with open(filename, "wb") as fp:
		pickle.dump(graph, fp)

def load(filename):
	"""
	Loads a pickled addr_graph object from disk.
	Args:
		filename (str): Location of graph to be loaded.
	Returns:
		G (addr_graph): The pickled addr_graph object.
	"""
	with open(filename, "rb") as fp:
		G = pickle.load(fp)
	return G
