import unicodecsv as csv
import matplotlib.pyplot as plt

def getBarChartData():
    f_artists = open('artists.csv') #opens artists.csv file
    f_albums = open('albums.csv') #opens albums.csv file 

    artists_rows = csv.reader(f_artists) #looks at rows from artists.csv and makes a new variable representing those rows
    albums_rows = csv.reader(f_albums) #same logic as above but applied to albums.csv

    artists_header = artists_rows.next() #skips the first row (header) and moves on to the next item in artists_rows
    albums_header = albums_rows.next() #same logic as above but applied to albums_rows

    artist_names = [] #creating an empty list called artist name (but I got a blank space baby and I'll write your name) 
    
    decades = range(1900,2020, 10) #sets specified range of decades in ten year increments
    decade_dict = {} #creates a blank dictionary to be filled
    for decade in decades:
        decade_dict[decade] = 0 #the dictionary keys are equal to the decades where the set values are equal to zero 
    
    for artist_row in artists_rows: #for loop setting for each row in artists_rows, sets variable artist_row equal to four variables listed in the row
        if not artist_row: #skips data that doesnt appear in artists_row
            continue
        artist_id,name,followers, popularity = artist_row
        artist_names.append(name) #appends artist name to the list artist_names

    for album_row  in albums_rows: #for loop setting for each row in album_rows, set the variable album_row equal to five variables listed in the row 
        if not album_row: #skips for loop if data does appear 
            continue
        artist_id, album_id, album_name, year, popularity = album_row
        for decade in decades:
            if (int(year) >= int(decade)) and (int(year) < (int(decade) + 10)): #if the year is within a specific decade 
                decade_dict[decade] += 1 #add one to the number of albums from that decade to values in the decade dictionary 
                break

    x_values = decades #x values are decades
    y_values = [decade_dict[d] for d in decades] #y values are equal to the counts of albums within the specified decades
    return x_values, y_values, artist_names #returns x_values, y_values, and the list of artist_names 

def plotBarChart():
    x_vals, y_vals, artist_names = getBarChartData() #grabs x and y values and artists names list from the function above
    
    fig , ax = plt.subplots(1,1) #draws a figure with one subplot
    ax.bar(x_vals, y_vals, width=10) #plots x and y values  
    ax.set_xlabel('decades') #labels the x axis as decades
    ax.set_ylabel('number of albums') #labels the y axis as numner of albums
    ax.set_title('Totals for ' + ', '.join(artist_names)) #sets title as Totals for__ which fills in the artist names from the artist_names list
    plt.show() #displays the bar chart 


    
