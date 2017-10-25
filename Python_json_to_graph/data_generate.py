# Using python 2.7
# May need to modify for python 3

import json

def get_addr_value(tx):
	"""
	Returns addresses and values associated to a transaction.
	Parameters:
		tx: transaction JSON (python dictionary)
	Returns:
		in_addr: list of sending addresses
			* one per input transaction
			* not necessarily distinct
		in_value: list of values (in Satoshi) of each input transaction
			* in_value[i] corresponds to in_addr[i]
		out_addr: list of receiving addresses
		out_value: list of values (in Satoshi) for each recipient
			* out_value[i] corresponds to out_addr[i]
	"""
	# initialize lists
	in_addr, in_value, out_addr, out_value = [], [], [], []
	# if input transaction exists (otherwise coin base)
	if "prev_out" in tx["inputs"][0].keys():
		# get list of input transactions
		prev_out = tx["inputs"][0]["prev_out"]
		# if single input transaction,
		# then prev_out is not a list;
		# so wrap it in a list
		if type(prev_out) == dict: prev_out = [prev_out]
		# for each input transaction t
		for t in prev_out:
			# if input address exists
			if "addr" in t.keys():
				# store input address
				in_addr.append(t["addr"])
				# store associated value
				in_value.append(t["value"])
	# for each output transaction t
	for t in tx["out"]:
		# if output address (recipient) exists
		if "addr" in t.keys():
			# store output address
			out_addr.append(t["addr"])
			# store associated value
			out_value.append(t["value"])
	# return addresses and values
	return in_addr, in_value, out_addr, out_value


# load block.json into python dictionary
with open("block.json", "rb") as fp:
	block = json.load(fp)

# take the subdictionary of transactions
transactions = block["tx"]

# open a file to write data to
# we will write lines of the form:
# input_address output_address transaction_value

file = open("data.csv", "w")

# initialize variable for counting number of transactions with multiple inputs
multi_inputs = 0
# for each transaction in the block
for tx in transactions:
	# get associated addresses and values
	in_addr, in_value, out_addr, out_value = get_addr_value(tx)
	# if no input addresses
	if len(in_addr) == 0:
		# then for each output address
		for j in range(len(out_addr)):
			# record as coin base transaction
			file.write("base, "+out_addr[j]+", "+str(out_value[j])+"\r\n")
	# else if input address exists
	else:
		# delete duplicate addresses
		in_addr = list(set(in_addr))
		# update if multiple distinct input addresses
		if len(in_addr) >= 2: multi_inputs += 1
		# for each distinct input address
		# (there should only be one, else bug)
		for i in range(len(in_addr)):
			# for each output address
			for j in range(len(out_addr)):
				# record transaction
				file.write(in_addr[i]+", "+out_addr[j]+", "+str(out_value[j])+"\r\n")

# close file
file.close()

# print number of transactions with multiple distinct input addresses
print multi_inputs