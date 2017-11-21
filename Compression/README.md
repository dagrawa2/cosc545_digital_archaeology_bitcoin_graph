This directory contains some compression tools implemented in python-- in particular, compression to .gz and .tar.gzz formats.

You are free to use command line tools to do your compression; in that case, just ignore this directory. But you feel more comfortable with python scripts, then this directory is for you.

API:

1. Suppose you want to compress foo.csv to foo.csv.gz. Run the following command:
	python gz.py foo.csv
Note gz.py must be placed in the same directory as foo.csv. Also, the original file foo.csv will not be altered; a second compressed file foo.csv.gz will be created.

2. Suppose you have a folder Foo containing files foo1.csv, foo2.csv, etc. Suppose you want to create a copy of this folder containing compressions of the files. Run the command
	python gz_all.py Foo
This will create a new directory Foo_gz containing files foo1.csv.gz, foo2.csv.gz, etc.

3. Suppose you have a folder Foo containing files foo1.csv, foo2.csv, etc. Suppose you want to archive and compress this folder to .tar.gz format. Run the command
	python targz.py Foo
The result is the file Foo.tar.gz.
