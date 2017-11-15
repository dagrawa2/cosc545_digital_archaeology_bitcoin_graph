from __future__ import division
import networkx as nx
import graph_tools as gt

G = gt.load("graph")

#print "order: ", G.order()
#print "max in-degree: ", max(G.in_degree().values())
#print "max out-degree: ", max(G.out_degree().values())
#print "longest path length: ", nx.dag_longest_path_length(G)

#H = G.subgraph([N for N in G.nodes() if G.in_degree(N)>=2])
#path = nx.dag_longest_path(H)
#H = None

#path.sort()
#path.reverse()
#N = path[0]
#for M in path[1:]:
#	print G.back_flow(N, M)

path = nx.dag_longest_path(G)
path.sort()
path.reverse()
print path[-1]