from typing import ItemsView
import spotipy
from spotipy.client import Spotify
from spotipy.oauth2 import SpotifyClientCredentials
import ytmdl
import inspect
import youtube_dl
import os
import re
birdy_uri = 'spotify:artist:2WX2uTcsvV5OnS0inACecP'

directory = "/Users/mac/music"
files = os.listdir(directory)
for file in files: 
    name = file
    name = re.sub(' ', '#', name)
    os.rename(directory + "/" + file, directory + "/" + name)


cid = '54c1337eb64946fabb980c013876cf62'
secret = 'ad7b6cd473b746ca89641171c371758e'
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
results = spotify.artist_albums(birdy_uri, album_type='album')
albums = results['items']
spo = Spotify()
#playlist id "6zCq1yEz4uisYoKT2faO5I"

#this is the "Morning Bluestpanda's" id list
pID = "spotify:playlist:6zCq1yEz4uisYoKT2faO5I"

#Jordan smith
# pID = "spotify:playlist:3MhNuSt8uRLn46yXvjFnZa"

list = spotify.playlist_items(pID, fields='items.track.name, total, name, items.track.uri, items.track.artists.name')

#this is to write all the names in the list 
list['items'].reverse()
for i in list['items']:
    os.system("ytmdl " + " -q " + str(i['track']['name']) + " " +  str(i['track']['artists'][0]['name']))
    print("NAME: " + str(i['track']['name']))

directory = "/Users/mac/music"
files = os.listdir(directory)
for file in files: 
    name = file
    name = re.sub('#', ' ', name)
    os.rename(directory + "/" + file, directory + "/" + name)


