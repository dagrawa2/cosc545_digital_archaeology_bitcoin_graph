import gzip
import os
import shutil
import sys

folder = sys.argv[1]
if not os.path.exists(folder+"_gz"):
	os.makedirs(folder+"_gz")

filenames = os.listdir(folder)
for filename in filenames:
	print "compressing "+folder+"/"+filename+" . . . "
	with open(folder+"\\"+filename, "rb") as f_in, gzip.open(folder+"_gz\\"+filename+".gz", "wb") as f_out:
		shutil.copyfileobj(f_in, f_out)
