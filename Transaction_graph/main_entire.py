# Using python 2.7
import data_tools as dt
import graph_tools as gt

# initial block hash
block_hash = "0000000000000000002ba18935b6e5e2945a1558b24633ff520045995c736f92"

# generate CSV data for three blocks up to the above hash
dt.build_entire_csv(block_hash, "data.csv", num_blocks=5)

# initialize transaction graph object
G = gt.tx_graph()

# build graph from CSV data
G.read_data("data.csv")

# save graph object to disk
gt.save(G, "graph")

# test gt.load by clearing the variable G
# and then loading it back from disk
G = None
G = gt.load("graph")

# print some graph attributes
print "order: ", G.order()
print "max in-degree: ", max(G.in_degree().values())
print "max out-degree: ", max(G.out_degree().values())
import networkx as nx
print "longest path length: ", nx.dag_longest_path_length(G)