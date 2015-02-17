import sys
import requests
import csv
import itertools 
from bs4 import BeautifulSoup

def getRelatedArtists(artistId):
	url_base = 'https://api.spotify.com'
	url_addon = '/v1/artists/'
	related_artist = artistId + '/related-artists'
	url = url_base + url_addon + related_artist
	#print url 
	req = requests.get(url)
	assert req.ok 
	returned_data = req.json()
	get_artist = returned_data["artists"]
	get_related_artistId = []
	actually_get_related_artistId = []
	for i in range(len(get_artist)): 
		get_related_artist = get_artist[i]
		get_id = get_related_artist['id']
		get_related_artistId.append(get_id)
	return get_related_artistId

#artistId = '4UEhWRcA8NyjX0xaGjYf19'
#getRelatedArtists(artistId)


def getDepthEdges(artistID, depth):
	tuple_artist_list = []
	related_ids = []
	related_ids.append(artistID)
	for i in range(depth):
		for ids in related_ids:
			depth_artist_list = getRelatedArtists(ids)
			for artist in depth_artist_list:
				tupl = (ids, artist)
				tuple_artist_list.append(tupl)
			related_ids = depth_artist_list
	remove_duplicates_list = tuple_artist_list
	#set(remove_duplicates_list)
	list(set(remove_duplicates_list))
	return(remove_duplicates_list)

#artistID = '4UEhWRcA8NyjX0xaGjYf19'

#print getDepthEdges(artistID, 2)

import pandas as pd 
import numpy as np

def getEdgeList(artistID, depth):
	edgelistthing = pd.DataFrame(getDepthEdges(artistID, depth))
	return edgelistthing 

#artistID = '2mAFHYBasVVtMekMUkRO9g'
#getEdgeList(artistID, 2)



def writeEdgeList(artistID, depth, filename):
	data = getEdgeList(artistID, depth)
	saved_csv_file = data.to_csv(filename, index = False)

writeEdgeList('2mAFHYBasVVtMekMUkRO9g', 2, 'out.csv')
	



	



	

