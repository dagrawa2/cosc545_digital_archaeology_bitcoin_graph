import sys

file = open(sys.argv[1], "r")
lines = file.readlines()
file.close()

lines = [line for line in lines if len(line) > 0]
print len(lines[1:])
