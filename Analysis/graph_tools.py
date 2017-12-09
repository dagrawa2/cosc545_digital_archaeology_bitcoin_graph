# Using python 2.7
import networkx as nx
import pandas as pd
import pickle

class tx_graph(nx.DiGraph):
	"""
	This class defines a directed graph object
	whose nodes represent unique bitcoin transaction indeces (on blockchain.info) and
	whose edges represent input transaction values.
	This class inherits from the nx.DiGraph class.
	"""
	
	def __init__(self):
		"""
		Initializes a graph object.
		"""
		nx.DiGraph.__init__(self)

	def read_data(self, filename, compression="infer"):
		"""
		Builds graph from edge data recorded in filename.
		Args:
			filename (str): Filename of CSV data.
		"""
		# read data
		data = pd.read_csv(filename, compression=compression)
		data = data.dropna()
		# first column is input transactions
		inputs = list(data.iloc[:,0].values)
		# second column is output transactions
		outputs = list(data.iloc[:,1].values)
		# third column is input transaction values
		values = list(data.iloc[:,2].values)
		# fourth column is probability that
		# a bitcoin belonging to the output transaction
		# came from the input transaction
		probs = list(data.iloc[:,3].values)
		# add a node for every transaction in the data
		self.add_nodes_from(list(set(inputs+outputs)))
		# for each line in the data
		for i in range(len(inputs)):
			# draw an edge between transactions weighted by value and probability
			self.add_edge(int(inputs[i]), int(outputs[i]), value=int(values[i]), p=float(probs[i]))

	def back_flow(self, tx_leaf, tx_root):
		ancestors = set([tx_leaf]).union(nx.ancestors(self, tx_leaf))
		descendants = set([tx_root]).union(nx.descendants(self, tx_root))
		H = self.subgraph(ancestors.intersection(descendants))
		ancestors, descendants = None, None
		if len(H.nodes()) == 0:
			return 0
		nx.set_node_attributes(H, "temp", 1)
		layers = create_layers(H)
		for layer in layers[1:]:
			for T in layer:
				H.node[T]["temp"] = sum([H.edge[T][U]["p"]*H.node[U]["temp"] for U in H.successors(T)])
		return H.node[tx_root]["temp"]

	def gen_flow_data(self, tx_leaf, filename, max_distance=None):
		if self.in_degree(tx_leaf) == 0:
			file = open(filename, "w")
			file.write("distance,flow\n")
			file.write("0,1")
			file.close()
			return
		ancestors = set([tx_leaf]).union(nx.ancestors(self, tx_leaf))
		H = self.subgraph(ancestors)
		ancestors = None
		nx.set_node_attributes(H, "distance", 0)
		nx.set_node_attributes(H, "flow", 1)
		layers = create_layers(H)
		if max_distance: layers = layers[:max_distance+1]
		distance = 0
		file = open(filename, "w")
		file.write("distance,flow\n")
		for layer in layers[1:]:
			distance += 1
			for T in layer:
				H.node[T]["distance"] = distance
				H.node[T]["flow"] = sum([H.edge[T][U]["p"]*H.node[U]["flow"] for U in H.successors(T)])
				file.write(str(H.node[T]["distance"])+","+str(H.node[T]["flow"])+"\n")
		file.close()
		return

def create_layers(G):
	H = nx.DiGraph(G)
	layers = []
	for i in range(H.order()):
		L = [N for N in H.nodes() if H.out_degree(N) == 0]
		layers.append(L)
		H.remove_nodes_from(L)
		if H.nodes() == []:
			break
	return layers


def save(graph, filename):
	"""
	Pickles a tx_graph object to filename.
	Args:
		graph (tx_graph): Graph to be pickled.
		filename (str): Filename where graph will be written.
	"""
	with open(filename, "wb") as fp:
		pickle.dump(graph, fp)

def load(filename):
	"""
	Loads a pickled tx_graph object from disk.
	Args:
		filename (str): Location of graph to be loaded.
	Returns:
		G (tx_graph): The pickled tx_graph object.
	"""
	with open(filename, "rb") as fp:
		G = pickle.load(fp)
	return G
