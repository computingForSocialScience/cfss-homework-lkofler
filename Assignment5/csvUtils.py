from io import open
import csv

def writeArtistsTable(artist_info_list):
    """Given a list of dictionaries, each as returned from 
    fetchArtistInfo(), write a csv file 'artists.csv'.

    The csv file should have a header line that looks like this:
    ARTIST_ID,ARTIST_NAME,ARTIST_FOLLOWERS,ARTIST_POPULARITY
    """
    f = open('artists.csv', 'w')
    f.write(u'ARTIST_ID,ARTIST_NAME,ARTIST_FOLLOWERS,ARTIST_POPULARITY\n')
    for line in artist_info_list:
        artist_id = str(line['artist_idd'])
        artist_name = line['name']
        artist_followers = str(line['followers'])
        artist_popularity = str(line['popularity'])
        """f.write(artist_id)
        f.write(artist_name)
        f.write(artist_followers)
        f.write(artist_popularity)
        f.write('\n')
        f.write([artist_id, u',', artist_name, u',', artist_followers, u',', artist_popularity,u'\n'])"""

        s=artist_id+','+'"'+artist_name+'"'+','+artist_followers+','+artist_popularity+'\n'
        f.write(s)
        
    f.close()

#artist_info_list = [{'genres': [u'riot grrrl'], 'popularity': 44, 'followers': 12431, 'id': u'0gvHPdYxlU94W7V5MSIlFe', 'name': u'Bikini Kill'}]
#writeArtistsTable(artist_info_list)

      
def writeAlbumsTable(album_info_list):
    """
    Given list of dictionaries, each as returned
    from the function fetchAlbumInfo(), write a csv file
    'albums.csv'.

    The csv file should have a header line that looks like this:
    ARTIST_ID,ALBUM_ID,ALBUM_NAME,ALBUM_YEAR,ALBUM_POPULARITY
    """
    f = open('albums.csv', 'w')
    f.write(u'ARTIST_ID,ALBUM_ID,ALBUM_NAME,ALBUM_YEAR,ALBUM_POPULARITY\n')
    for line in album_info_list:
        artist_id = str(line['artist_id'])
        album_id = line['album_id']
        album_name = line['name']
        album_year = str(line['year'])
        album_popularity = str(line['popularity'])
        s=artist_id+','+album_id+','+'"'+album_name+'"'+','+album_year+','+album_popularity+'\n'
        f.write(s)
        
    f.close()

#album_info_list = [{'popularity': 53, 'artist_id': u'6olE6TJLqED3rqDCT0FyPh', 'year': u'1993', 'name': u'In Utero - 20th Anniversary Super Deluxe', 'album_id': '14VVqBoDw1SxoNLW3Cj3mN'}]
#writeAlbumsTable(album_info_list)
