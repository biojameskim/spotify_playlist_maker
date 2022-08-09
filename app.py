import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json

scope = 'playlist-modify-public'
username = 'biojameskim2002'

token = SpotifyOAuth(scope=scope, username=username)
spotifyObject = spotipy.Spotify(auth_manager = token)

# create the playlist
playlist_name = input("Enter a playlist name: ")
playlist_description = input("Enter a playlist description: ")

spotifyObject.user_playlist_create(user=username,name=playlist_name,description=playlist_description,public=True)

user_input = input("Enter the song: ")
list_of_songs = []

while user_input != 'quit':
    result = spotifyObject.search(q=user_input)
    list_of_songs.append(result['tracks']['items'][0]['uri'])
    user_input = input("Enter the song: ")

# Get the playlist we just created
pre_playlist = spotifyObject.user_playlists(user=username)
playlist_id = pre_playlist['items'][0]['id']

# Add songs to the playlist
spotifyObject.user_playlist_add_tracks(user=username,playlist_id=playlist_id,tracks=list_of_songs)