The files in this directory demonstrate a proof of principle that a graph of bitcoin addresses can be constructed using the blockchain.info API. The end result is a graph whose nodes are labelled as bitcoin addresses and whose directed edges represent bitcoin transactions weighted by value. This is again only a proof of principle; we will probably want to attach more metadata to the nodes and edges, we will have to deal with possible errors in the future when parsing JSON files, and we will also need to worry about scaling to larger data sets.

The file "block_retrieve.py" uses the blockchain.info API to download one block and save it as "block.json".

The file "data_generate.py" parses "block.json" and extracts the addresses and values associated to every transaction in the block. The results are stored in "data.csv"; each line in this file has the form:
	input_address, output_address, transaction_value
Note this is very basic; we do not store the transaction hash or anything.

The file "graph_generate.py" implements a class for a bitcoin address graph that inherits from the "DiGraph" class from the python networkx module. The address graph class contains a method to build a graph from .csv data. We build a graph from data.csv and save the resulting object to "graph.grph" (a pickled python object). This way, the graph has to be constructed only once.

The file "graph_analyze.py" reads in the constructed graph from "graph.grph" and prints out a few very simple graph attributes such as the number of nodes and the address with the most outgoing transactions.