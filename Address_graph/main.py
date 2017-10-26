# Using python 2.7
import data_tools as dt
import graph_tools as gt

# example block hash
block_hash = "0000000000000000002ba18935b6e5e2945a1558b24633ff520045995c736f92"

# save block JSON with above hash to disk
dt.save_block(block_hash, "block.json")

# generate CSV data from local file block.json
dt.build_csv("block.json", "data.csv", local=True)

# initialize address graph object
G = gt.addr_graph()
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