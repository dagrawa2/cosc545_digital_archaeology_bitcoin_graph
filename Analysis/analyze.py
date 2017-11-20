from __future__ import division
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import os
import pandas as pd
import graph_tools as gt

def freqs(L):
	D = {l:0 for l in list(set(L))}
	for l in L:
		D[l] += 1
	return D

file = open("Graph_data\\attributes.csv", "w")
filenames = os.listdir("Collected_data")

headers = ["year", "month", "day", "order", "minInDegree", "maxInDegree", "meanInDegree", "stdInDegree", "minOutDegree", "maxOutDegree", "meanOutDegree", "stdOutDegree", "minComp", "maxComp", "meanComp", "stdComp", "longestPathLength", "minFlow", "maxFlow", "meanFlow", "stdFlow"]

line = ""
for header in headers:
	line += header+","
line = line[:-1]+"\n"
file.write(line)

for filename in filenames:
	print "Processing "+filename+" . . . "
	D = {}
	D.update({ \
	"year": int(filename[:4]), \
	"month": int(filename[5:7]), \
	"day": int(filename[8:10]) \
	})
	print "\tBuilding graph . . . "
	G = gt.tx_graph()
	G.read_data("Collected_data\\"+filename)
	print "\tProcessing in-degree distribution . . . "
	in_degrees = np.array([d for d in G.in_degree().values() if d > 0])
	in_degree_freqs = freqs(in_degrees)
	fp = open("In_degree_distros\\"+filename, "w")
	fp.write("inDegree,frequency\n")
	for key in sorted(in_degree_freqs.keys()):
		fp.write(str(key)+","+str(in_degree_freqs[key])+"\n")
	fp.close()
	D.update({ \
	"order": G.order(), \
	"minInDegree": np.min(in_degrees), \
	"maxInDegree": np.max(in_degrees), \
	"meanInDegree": np.mean(in_degrees), \
	"stdInDegree": np.std(in_degrees), \
	})
	print "\tProcessing out-degree distribution . . . "
	out_degrees = np.array([d for d in G.out_degree().values() if d > 0])
	out_degree_freqs = freqs(out_degrees)
	fp = open("Out_degree_distros\\"+filename, "w")
	fp.write("outDegree,frequency\n")
	for key in sorted(out_degree_freqs.keys()):
		fp.write(str(key)+","+str(out_degree_freqs[key])+"\n")
	fp.close()
	D.update({ \
	"minOutDegree": np.min(out_degrees), \
	"maxOutDegree": np.max(out_degrees), \
	"meanOutDegree": np.mean(out_degrees), \
	"stdOutDegree": np.std(out_degrees), \
	})
	print "\tProcessing component sizes distribution . . . "
	comps = np.array([len(c) for c in nx.connected_components(G.to_undirected())])
	comp_freqs = freqs(comps)
	fp = open("Comp_distros\\"+filename, "w")
	fp.write("componentSize,frequency\n")
	for key in sorted(comp_freqs.keys()):
		fp.write(str(key)+","+str(comp_freqs[key])+"\n")
	fp.close()
	D.update({ \
	"minComp": np.min(comps), \
	"maxComp": np.max(comps), \
	"meanComp": np.mean(comps), \
	"stdComp": np.std(comps) \
	})
	print "\tProcessing flow distribution . . . "
	path = sorted(nx.dag_longest_path(G))
	length = len(path)
	G.gen_flow_data(path[-1], "Flow_distros\\"+filename, max_distance=min(50, length))
	flow = pd.read_csv("Flow_distros\\"+filename)
	flow = flow.as_matrix()[:,1]
	D.update({ \
	"longestPathLength": length, \
	"minFlow": np.min(flow), \
	"maxFlow": np.max(flow), \
	"meanFlow": np.mean(flow), \
	"stdFlow": np.std(flow) \
	})
	print "\tWriting to csv file . . . "
	line = ""
	for header in headers:
		line += str(D[header])+","
	line = line[:-1]+"\n"
	file.write(line)

file.close()
print "Done!"
