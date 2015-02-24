import pandas as pd
import numpy as np
import networkx as nx 

def readEdgeList(filename):
	edgelist = pd.read_csv(filename)
	if len(edgelist.columns) != 2 :
		return "Edge list should have 2 columns"
		edgelist = pd.read_cvs(filename, usecols = [0,1])
		dataframe = pd.DataFrame(edgelist)
	else:
		dataframe = pd.DataFrame(edgelist)
	return dataframe 

#filename = 'out.csv'
#readEdgeList(filename) 

def degree(edgelist, in_or_out):
	if in_or_out == 'out':
		df = edgeList['0'].value_counts()
	elif in_or_out == 'in':
		df = edgeList['1'].value_counts()
	else:
		print "Tell it in or out" 
	return df

#in_or_out = 'out'
#filename = 'out.csv'
#edgeList = readEdgeList(filename)
#print degree(edgeList, in_or_out)

def combineEdgeLists(edgeList1, edgeList2):
	pieces = [edgeList1, edgeList2]
	concatenated = pd.concat(pieces)
	combined = concatenated.drop_duplicates()
	return combined 

def pandasToNetworkX(edgeList):
	g = nx.DiGraph()
	for artist, related_artist in edgeList.to_records(index=False):
		g.add_edge(artist, related_artist)
	return g 

def randomCentralNode(inputDiGraph):
	centrality_dict = nx.eigenvector_centrality(inputDiGraph)
	normalization = sum(centrality_dict.values())
	for key in centrality_dict:
		try:
			centrality_dict[key] = centrality_dict[key]/float(normalization)
		except ZeroDivisionError:
			centrality_dict[key] = 1.0/len(centrality_dict)
	random_node = np.random.choice(centrality_dict.keys(), p=centrality_dict.values())
	return random_node


