# Using python 2.7
from __future__ import division
import json
import requests as req
import time
from os.path import exists

def save_block(block_hash, filename):
	"""
	Retrieves the block JSON with hash block_hash and
	writes it to filename.
	Args:
		block_hash (str): Hash of the block to be retrieved.
		filename (str): Filename where the block will be written.
			This should be a .json file.
	"""
	r = req.get("https://blockchain.info/rawblock/"+block_hash)
	with open(filename, "wb") as fp:
		fp.write(r.content)


def handle_duplicates(L_tx, L_value):
	"""
	Produces a list of _unique_ input transactions and associated values.
	Args:
		L_tx (list): List of input transactions, not necessarily unique.
		L_value (list): List of associated values:
	Returns:
		(list): List of unique input transactions
		(list): List of associated values.
	"""
	# create dictionary of unique transactions with initial values 0
	D = {tx:0 for tx in list(set(L_tx))}
	# for each value in L_value,
	# add it to the appropriate transaction in D
	for i in range(len(L_value)):
		D[L_tx[i]] += L_value[i]
	return D.keys(), D.values()

def get_tx_value(tx):
	"""
	Returns input transaction indeces and values associated to a transaction.
	Args:
		tx (dict): Transaction JSON.
	Returns:
		in_tx (list): List of input transaction indeces.
		in_value (list): List of values (in Satoshi) that each input transaction holds.
			The ith value is held by the ith input transaction.
	"""
	# initialize lists
	in_tx, in_value = [], []
	# for each input
	for input in tx["inputs"]:
		# if sending address exists
		# (otherwise coin base or empty value)
		if "prev_out" in input.keys() and "addr" in input["prev_out"].keys():
			# record input transaction index and value
			in_tx.append(input["prev_out"]["tx_index"])
			in_value.append(input["prev_out"]["value"])
	#if no input transactions
	if len(in_tx) == 0:
		# designate -1 as index of coin base
		in_tx.append(-1)
		# coin base value is value of output transactions
		in_value.append(sum([out_trans["value"] for out_trans in tx["out"]]))
	# handle duplicate input transactions
	in_tx, in_value = handle_duplicates(in_tx, in_value)
	return in_tx, in_value

def build_entire_csv(block_hash, filename_csv, num_blocks=1):
	"""
	Generates a CSV data file from multiple blocks for building a transaction graph;
	the headers of the CSV file are:
	InputTransactionIndex, OutputTransactionIndex, Value, BackFlowProbability.
	Args:
		block_hash (str): Hash of the most recent block from which data is to be extracted.
		filename_csv (str): Filename where the CSV data will be written.
		num_blocks (int): Number of blocks from which data is to be extracted.
			This includes block_hash and the num_blocks-1 blocks preceding it.
		append (boole): If False, then filename_csv is opened in "w" mode.
			If True, then filename_csv is opened in "a" mode.
			Column headers are written only if False.
	"""
	file = open(filename_csv, "a")
	filename_log = filename_csv.split('.')[0]
	filename_log = filename_log + '.log'
	log = open(filename_log, "a")
	# loop over initial and previous blocks
	for count in range(num_blocks):
		print "Getting block "+str(count+1)+" . . . "
		# get block JSON from blockchain.info API
		r = req.get("https://blockchain.info/rawblock/"+block_hash)
		try:	
			block = json.loads(r.content)
		except:
			print 'Caught API block'
			time.sleep(30)
			r = req.get("https://blockchain.info/rawblock/"+block_hash)
			block = json.loads(r.content)
		# for each transaction in block
		for tx in block["tx"]:
			# get input transaction indeces and values
			in_tx, in_value = get_tx_value(tx)
			# get total input value
			total_input = sum(in_value)
			# for each input transaction index
			for i in range(len(in_tx)):
				# record edge data
				file.write(str(in_tx[i])+","+str(tx["tx_index"])+","+str(in_value[i])+","+str(in_value[i]/total_input)+"\r\n")
		log.write(block_hash+"\r\n")
		print "Block "+str(count+1)+" complete!"
		# set to previous block
		block_hash = block["prev_block"]
		print "Waiting . . ."
		time.sleep(10)
	file.close()
