import sys
import requests
import csv
#from bs4 import BeautifulSoup

def fetchArtistId(name):
	url_base = 'https://api.spotify.com'
	url_addon = '/v1/search?q='
	artist = name + '&type=artist'
	url = url_base + url_addon + artist
	#print url 
	req = requests.get(url)
	assert req.ok 
	req_json = req.json()
	get_artist = req_json.get("artists")
	get_items = get_artist.get("items")
	#print get_items 
	get_id = get_items[0]
	artist_id = get_id['id']
	return artist_id

#artist = 'queen'
#print fetchArtistId(artist)

def fetchArtistInfo(artist_id):
	url_base = 'https://api.spotify.com/v1/artists/'
	url = url_base + artist_id
	req = requests.get(url)
	req_json = req.json()
	if req.ok ==False:
		print "Error"
	genres = req_json.get('genres')
	artist_followers = req_json.get('followers')
	followers = artist_followers['total']
	name = req_json.get('name')
	popularity = req_json.get('popularity')
	artist_idd = artist_id
	values = [followers, genres, artist_id, name, popularity]
	keys = ['followers', 'genres', 'artist_idd', 'name', 'popularity']
	artist_dict = dict(zip(keys,values))
	return artist_dict 

#artist_id = '1dfeR4HaWDbWqFHLkxsg1d'
#fetchArtistInfo(artist_id)




