# Using python 2.7
import sys
import data_tools as dt
from os.path import exists

if len(sys.argv) == 4:
        if exists("./"+sys.argv[2]):
                print "csv file "+sys.argv[2]+" exists, either delete it or use add_to_csv.py please"
                exit()
        file = open(sys.argv[2], "w")
        file.write("InputTransactionIndex,OutputTransactionIndex,Value,BackFlowProbability\r\n")
        filename_log = sys.argv[2].split('.')[0]
        filename_log = filename_log + '.log'
        log = open(filename_log, "w")
        log.write("Blocks logged in csv\r\n")
        dt.build_entire_csv(sys.argv[1], sys.argv[2], int(sys.argv[3]))
else:
        print('usage: python2.7, make_csv.py, start block hash, *.csv, number of blocks')


