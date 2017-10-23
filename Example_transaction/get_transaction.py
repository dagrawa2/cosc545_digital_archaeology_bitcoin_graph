# using python 2.7
# may need to modify for python 3

import json
import requests as req

tx_hash = "f555ffc47eb31a3ce7cb644c49650afe60d41440473bcb962d1afc505ab99a9a"
r = req.get("https://blockchain.info/rawtx/"+tx_hash)

with open("output.json", "wb") as out:
	out.write(r.content)
