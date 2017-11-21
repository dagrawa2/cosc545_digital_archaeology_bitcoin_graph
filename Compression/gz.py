import gzip
import shutil
import sys

filename = sys.argv[1]

print "compressing "+filename+" . . . "
with open(filename, "rb") as f_in, gzip.open(filename+".gz", "wb") as f_out:
	shutil.copyfileobj(f_in, f_out)
