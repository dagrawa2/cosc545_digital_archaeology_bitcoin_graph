from __future__ import division
import networkx as nx
import graph_tools as gt

G = gt.tx_graph()
G.read_data("bigger_data.csv")

path = nx.dag_longest_path(G)
path.sort()
path.reverse()

N = path[0]
G.gen_flow_data(N, "flow.csv")
