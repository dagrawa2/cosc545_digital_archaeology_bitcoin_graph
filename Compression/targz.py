import sys
import tarfile

folder = sys.argv[1]

print "compressing "+folder+" . . . "
tar = tarfile.open(folder+".tar.gz", "w:gz")
tar.add(folder, arcname=folder)
tar.close()
