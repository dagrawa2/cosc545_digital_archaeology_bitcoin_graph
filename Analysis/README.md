This directory contains a script called analyze.py that automates most of the data generation. After that, we just have to plot and look for trends or anything worth presenting.

Do NOT delete or rename any of the subdirectories. If no subdirectories exist, then create the following subdirectories:
	Collected_data
	Comp_distros
	Flow_distros
	Graph_data
	In_degree_distros
	Out_degree_distros
	Plots

Follow these steps:

1. You should have collected various 1000-block chunks of data. You collected each chunk starting with a block hash. Find the date associated to this seed block hash; you can just look up the hash on blockchain.info, and it will give you the time stamp. Rename the .csv file storing the chunk in the form
	year-month-day.csv.
For example, suppose I have a 1000-block chunk of data that I collected with a seed block hash dated January 7, 2015. Then I should name the file
	2015-01-07.csv.
Note the leading zeros for month and day; this is very important!

2. Place all your 1000-block chunk csv files in the subdirectory "Collected_data".

3. (For non-Windows users only). Open analyze.py. Use find-and-replace to replace all double backslashes (\\) with a single forward slash (/). This converts all path strings into unix style.

4. Run analyze.py (with python 2.7). This could take a long time; it works well on 100-block chunks, and I hope it scales well to 1000-block chunks!

5. Once analyze.py is finished executing, all subdirectories except Plots should be populated with data files.

So let me explain what analyze.py is doing and what data files it generates:

The file analyze.py loops over all files you placed in the Collected_data subdirectory. For each file, it generates a bunch of graph attributes and writes them to a single csv file. So the result is a file Graph_data/attributes.csv whose rows correspond to 1000-block chunks with different time stamps and whose columns are different graph attributes.

Here are the attributes generated for each 1000-block chunk:

1. year: analyze.py parses the name of each file in Collected_data and extracts the year of the first block hash. This is why renaming your csv files to time stamps is so important.

2. month: Analogous to year.

3. day: Analogous to year and month.

4. order: Once the date has been parsed, analyze.py builds the graph from the given csv data. It records the number of nodes.

5. minInDegree: Next, analyze.py builds the in-degree distribution of the graph (i.e., the number of parent nodes that each node has). The in-degree of 0 is dropped since this value is an artifact of or sampling; if we had the whole block chain, then the only node with in-degree 0 would be "coin base". Once the in-degree distro is obtained, its minimum is returned.

6. maxInDegree: max of the in-degree distro.

7. meanInDegree: mean of the in-degree distro.

8. stdInDegree: std of the in-degree distro. Also, a csv file containing the in-degree distribution is generated and saved in the In_degree_distro subdirectory. One csv file is generated for each time stamp listed in Collected_data; thus, you can view the degree distro for each of your 1000-block chunks.

9-12. We do the same as 5-8 but with the out-degree distribution. We again drop the value 0 since it is an artifact of our sampling. The distro is also saved in the Out_degree distro subdirectory.

13-16. components: The graph is disconnected and has many components. The script analyze.py gathers the sizes (orders) of all components and builds a distribution. The min, max, mean, and std are recorded as before. The distro for each time stamp is saved as csv in the Comp_distros subdirectory.

17. longestPathLength: analyze.py nexts finds the longest path in the graph and stores its length.

18-21: flow: The script finds the head T of the longest path found above. The script then calls gen_flow_data to compute the probability that each bitcoin belonging to T came from each one of its ancestors. The option is currently set so that the flow only goes back 50 generations; we do not consider flow along transaction chains longer than 50, as the probabilities approach 0 and are useless to record. As before, we save the flow data as csv in Flow_data and we record its min, max, mean, and std in the master csv Graph_data/attributes.csv.

So the end result is that we have the in-degree distros, out-degree distros, component size distros, and flow vs. distance data for all the 1000-block chunks you collected. You can plot these csvs to look for interesting features.

We also have a master csv in Graph_data that records the min, max, mean, and std of each of the above distros.

Once you are finished, send me your Graph_data/attributes.csv file (it shouldn't be heavy). I will compile everyone's data and sort the rows in chronological order. We can then plot these attributes vs time to see how the graph structure might have evolved over time.

I am currently working on other things as well. For example, it may be better to analyze not the entire 1000-block chunk but only its largest connected component. This would be most similar to a real "block chain". (note: the entire block chain would have been connected since all transactions ultimately connect back to the node "coin base"). This idea is a simple modification of this current directory. We can talk about it more tomorrow.
