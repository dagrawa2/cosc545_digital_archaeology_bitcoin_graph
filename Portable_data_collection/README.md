Hey all,

First, you need a 2.7 python environment and the requests module, you should have everything else you need already, please let me know if you have trouble setting this up, I will email you a virtualenv.  Too big for the gitHub though.

Only run one instance of make or add per computer or the API will block you more often than it's worth

These methods can collect data and deal with errors while you eat, work, sleep whatever, so keep collecting all day every day

We should discuss a way to divide and conquer different time chunks of the blockchain


Included in this toolkit are three files
1) A modified data_tools that collects block data, writes to csv, logs the write, and does so in the face of API limits,  PLEASE do not get rid of the sleep or write statements, you dont need to use this explicitly, the next two scripts will take care of that.

2) make_csv.py is called like this

	python2.7 make_csv.py #block hash# *.csv numBlocks

if you call with a csv that already exists it will fail, this prevents data corruption and overwriting.
NOTE  ***IMPORTANT*** call with numBlock > 1 or your .csv will be corrupted, looking into this issue

3) add_to_csv.py is called like this

	python2.7 add_to_csv.py *.csv numBlocks

if you call with a non-existent csv it will fail, this prevents data corruption and helps deter double collection
notice that no hash is required, for this function checks a .csv's log for the last hash recieved and starts there

AS LONG AS NO CODE IS CHANGED this folder can function as a store for everyone's individual data, Devanshu, notice that in the base repository there is a sample 100 block csv if you want to run graph experiments without bothering.
