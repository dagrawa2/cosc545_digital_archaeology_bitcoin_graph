# Using python 2.7
# May need to modify for python 3

import json
import requests as req

# Use blockchain.info API to retrieve block by hash

block_hash = "0000000000000000002ba18935b6e5e2945a1558b24633ff520045995c736f92"
r = req.get("https://blockchain.info/rawblock/"+block_hash)

# The result is in JSON format
# Save the block in a .json file

with open("block.json", "wb") as fp:
	fp.write(r.content)
