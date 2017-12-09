# Update: November 28, 2017

## What I Did

I downloaded the 2015, 2016, and 2017 data from dropbox. I did not use the 2014 data as I saw that some of the CSV files in the 2014 folder were very large, and I suspected that these particular CSV files contained more than 100 blocks.

I took all the CSV files from the 2015, 2016, and 2017 folders and compressed them to .csv.gz format. There were 23 files in all: May-December 2015, May-December 2016, and May-November 2017. I placed all 23 .csv.gz files into the Collected_data folder.

I modified analyze.py so it would uncompress .gz files on the fly. I ran analyze.py. This file loops over all files in Collected_data. For each file, the script analyze.py builds the 100-block transaction graph and records many of its attributes (see Analysis/README.md on github). It also records the time stamp for each 100-block chunk. The time stamp and graph attributes for each chunk are written into rows in Graph_data/data.csv.

In addition, analyze.py generates frequency data for in-degree, out-degree, component size, and bitcoin flow for each 100-block chunk. Each set of frequency data is a CSV file with the first column all unique values of an attribute (e.g., in-degree) and the second column the non-zero frequencies of these values. These CSV files are stored in the *-distros folders.

I wrote sort.py. This script reads in the data from Graph_data/data.csv and sorts the rows chronologically (just in case we decided to append 2014 data to data.csv later). The script also adds a new first column that simply indexes the rows with integers.

I wrote and ran plot_time.py. This generates the following image files stored in the Plots folder:
1. order.png: Plot of the 100-block graph order over time.
2. in_degree.py: Plot of the graph mean in_degree (plus standard deviation indicated by dashed curve) over time. I do not plot one unit standard deviation below the mean as the in-degree distribution for each month is highly skewed to small values so that standard deviation below the mean is useless.
3. out_degree.png: Analogous to in_degree.png but with out-degree.
4. comp.png: Analogous to in_degree.png but with component size.
5. flow.png: Analogous to in_degree.png but with flow.

I wrote plot_in_degree.py. This plots In_degree/2017-11-15.csv on a log-log scale up to in-degree 100; the in-degree plateaus after 100. The resulting image file is Plots/2017-11-15_in_degree.png. Please feel free to run this script again but for a different time stamp; if you do this, then make sure to change the time stamp both at the beginning of the file (in pd.read_csv) and at the end of the file (in fig.savefig).

I wrote and ran plot_out_degree.py and plot_comp.py in analogy to plot_in_degree.py.

I wrote plot_flow.py. This plots Flow_distros/2017-11-15.csv as a scatter plot; unlike the previous three plots, this plot is not a distribution but instead plots flow to see how it varies with distance.

Note: I do not feel like explaining what I mean by "flow". If you are not sure what I mean, then please ask me.


## Discussion

I looked at the plots (with some help from the eyes of others). Most of them are boring.

In-degree, out-degree, and component size are about constant with time. Their means are all very small but their distributions are very skewed.

Order increases with time. This is actually interesting. It means that 100-block chunks contain more and more transactions with time. This either means people are becoming more active as a whole (perhaps more users) or simply that people are prefering to mine larger blocks.

Mean flow is close to 0 initially but then begins to fluctuate between 0 and 1 after some time point. When flow is large, it means that there is a strong connection between transactions via bitcoin flow despite separation by many transaction links.

I plotted the in-degree, out-degree, and component size distributions on log-log scales. The curves are approximately linear. This indicates that these distributions follow power laws. We can then conclude that our 100-block transaction graphs are scale-free. This is a well-known fact about the bitcoin network and in fact holds for many large networks. The fact that we were able to reproduce these distributions means that we were able to capture some structure with 100-blocks that actually reflects the entire block chain.

The distance-flow plot for 2017-11-15 is interesting. The flow is 1.0 for distances up to about 23. After that, the flow drops to almost 0. This indicates that nodes are tightly connected in the sense of sharing common bitcoins for up to 23 transaction links. Flow diffuses beyond that. This is not as exciting as it looks. It could simply mean that the nodes for the first 23 transaction links were connected in a path with no additional children. In other words, we simply found a path of 23 single-input transactions.

In conclusion, we learned nothing surprising or interesting. We have no "real world" insights or "why should I care" responses. But we do have lots of data and pretty plots-- that counts, right?


# Update: November 30, 2017

## What I Did

I created four new scripts called plot_comp_all.py, plot_flow_all.py, plot_in_degree_all.py, and plot_out_degree_all.py. These scripts generate component size distributions, distance-flow scatter plots, in-degree distributions, and out-degree distributions for all 23 time stamps. Therefore, these scripts are just extensions of plot_comp.py, plot_flow.py, plot_in_degree.py, and plot_out_degree.py respectively.

the Plots folder contains the subfolders Comp_distros, Flow_distros, In_degree_distros, Out_degree_distros, and Time. The Time folder contains all the "over time" plots. The Flow_distros folder contains all the distance-flow scatter plots. The other three folders contain all the distributions.
