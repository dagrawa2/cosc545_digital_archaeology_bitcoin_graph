# Using python 2.7
import sys
import data_tools as dt
import json
from os.path import exists
import requests as req
import time

if len(sys.argv) == 3:
        if not exists("./"+sys.argv[1]):
                print "csv file "+sys.argv[1]+" doesn't exist, please use an existing file or make_csv.py"
		exit()
        print('getting last block collected and determining next block to be collected (prev) . . .')
	filename_log = sys.argv[1].split('.')[0]
        filename_log = filename_log + '.log'
	with open(filename_log, "r") as f:
		for line in f: pass
	"".join(line.split())
	print line
	r = req.get("https://blockchain.info/rawblock/"+line)
#	print r.content
	block = json.loads(r.content)
	block_hash = block["prev_block"]
	print('starting to add at block '+block_hash+' but first we wait . . .')
	time.sleep(10)	
	dt.build_entire_csv(block_hash, sys.argv[1], int(sys.argv[2]))
else:
        print('usage: python2.7, add_to_csv.py, *.csv, number of blocks to add')


