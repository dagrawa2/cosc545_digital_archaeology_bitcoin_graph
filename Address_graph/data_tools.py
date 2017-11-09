# Using python 2.7
from __future__ import division
import json
import requests as req

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


def handle_duplicates(L_addr, L_value):
	"""
	Produces a list of _unique_ addresses and associated values.
	Args:
		L_addr (list): List of addresses, not necessarily unique.
		L_value (list): List of associated values:
	Returns:
		(list): List of unique addresses
		(list): List of associated values.
	"""
	# create dictionary of unique addresses with initial values 0
	D = {addr:0 for addr in list(set(L_addr))}
	# for each value in L_value,
	# add it to the appropriate address in D
	for i in range(len(L_value)):
		D[L_addr[i]] += L_value[i]
	return D.keys(), D.values()

def get_addr_value(tx):
	"""
	Returns addresses and values associated to a transaction.
	Args:
		tx (dict): Transaction JSON.
	Returns:
		in_addr (list): List of sending addresses.
		in_value (list): List of values (in Satoshi) that each sending address sends.
			The ith value is sent by the ith sending address.
		out_addr (list): List of receiving addresses.
		out_value (list): List of values (in Satoshi) that each receiving address receives.
			The ith value is received by the ith receiving address.
	"""
	# initialize lists
	in_addr, in_value, out_addr, out_value = [], [], [], []
	# for each input transaction
	for input in tx["inputs"]:
		# if sending address exists
		# (otherwise coin base or empty value)
		if "prev_out" in input.keys() and "addr" in input["prev_out"].keys():
			# record address and value
			in_addr.append(input["prev_out"]["addr"])
			in_value.append(input["prev_out"]["value"])
	# for each output transaction
	for output in tx["out"]:
		# if receiving address exists
		# (otherwise empty value)
		if "addr" in output.keys():
			# record address and value
			out_addr.append(output["addr"])
			out_value.append(output["value"])
	# handle duplicate addresses
	in_addr, in_value = handle_duplicates(in_addr, in_value)
	out_addr, out_value = handle_duplicates(out_addr, out_value)
	return in_addr, in_value, out_addr, out_value


def build_csv(block_hash_or_file, filename_csv, local=False, append=False):
	"""
	Generates a CSV data file for building an address graph;
	the headers of the CSV file are:
	InputAddress, OutputAddress, TransactionIndex, ExpectedValue.
	Args:
		block_hash_or_file (str): Block hash (default) or filename of a block JSON.
			This is the source of the data.
		filename_csv (str): Filename where the CSV data will be written.
		local (boole): If False, then block_hash_or_file is read as a hash,
			and the block JSON is retrieved from blockchain.info.
			If True, then block_hash_or_file is read as a filename,
			and the block JSON is loaded from the specified location.
		append (boole): If False, then filename_csv is opened in "w" mode.
			If True, then filename_csv is opened in "a" mode.
			Column headers are written only if False.
	"""
	if append == True:
		# open CSV file in "a" mode
		file = open(filename_csv, "a")
	else:
		# open a fresh CSV file and write headers
		file = open(filename_csv, "w")
		file.write("InputAddress,OutputAddress,TransactionIndex,ExpectedValue\r\n")
	if local == True:
		# load block JSON from local file
		with open(block_hash_or_file, "rb") as fp:
			block = json.load(fp)
	else:
		# get block JSON from blockchain.info API
		r = req.get("https://blockchain.info/rawblock/"+block_hash_or_file)
		block = json.loads(r.content)
	# for each transaction in block
	for tx in block["tx"]:
		# get addresses and values
		in_addr, in_value, out_addr, out_value = get_addr_value(tx)
		# if no input addresses
		if len(in_addr) == 0:
			# for each output address
			for j in range(len(out_addr)):
				# record as coin base transaction
				file.write("base,"+out_addr[j]+","+str(tx["tx_index"])+","+str(out_value[j])+"\r\n")
		# if input addresses exist
		else:
			# get total input value
			total_input = sum(in_value)
			# for each input address and each output address
			for i in range(len(in_addr)):
				for j in range(len(out_addr)):
					# record transaction with _expected_ value
					file.write(in_addr[i]+","+out_addr[j]+","+str(tx["tx_index"])+","+str(out_value[j]*in_value[i]/total_input)+"\r\n")
	file.close()

def build_entire_csv(block_hash, filename_csv, num_blocks=1, append=False):
	"""
	Generates a CSV data file from multiple blocks for building an address graph;
	the headers of the CSV file are:
	InputAddress, OutputAddress, TransactionIndex, ExpectedValue.
	Args:
		block_hash (str): Hash of the most recent block from which data is to be extracted.
		filename_csv (str): Filename where the CSV data will be written.
		num_blocks (int): Number of blocks from which data is to be extracted.
			This includes block_hash and the num_blocks-1 blocks preceding it.
		append (boole): If False, then filename_csv is opened in "w" mode.
			If True, then filename_csv is opened in "a" mode.
			Column headers are written only if False.
	"""
	if append == True:
		# open CSV file in "a" mode
		file = open(filename_csv, "a")
	else:
		# open a fresh CSV file and write headers
		file = open(filename_csv, "w")
		file.write("InputAddresses,OutputAddresses,TransactionHash,ExpectedValue\r\n")
	# loop over initial and previous blocks
	for count in range(num_blocks):
		print "Getting block "+str(count)+" . . . "
		# get block JSON from blockchain.info API
		r = req.get("https://blockchain.info/rawblock/"+block_hash)
		block = json.loads(r.content)
		# for each transaction in block
		for tx in block["tx"]:
			# get addresses and values
			in_addr, in_value, out_addr, out_value = get_addr_value(tx)
			# if no input addresses
			if len(in_addr) == 0:
				# for each output address
				for j in range(len(out_addr)):
					# record as coin base transaction
					file.write("base,"+out_addr[j]+","+str(tx["tx_index"])+","+str(out_value[j])+"\r\n")
			# if input addresses exist
			else:
				# get total input value
				total_input = sum(in_value)
				# for each input address and each output address
				for i in range(len(in_addr)):
					for j in range(len(out_addr)):
						# record transaction with _expected_ value
						file.write(in_addr[i]+","+out_addr[j]+","+str(tx["tx_index"])+","+str(out_value[j]*in_value[i]/total_input)+"\r\n")
		print "Block "+str(count)+" complete!"
		# set to previous block
		block_hash = block["prev_block"]
	file.close()
