import spotipy
import json
from spotipy.oauth2 import SpotifyOAuth


# Playlist and psotify data
data = {}
with open('./resources/config.json', 'r') as data_file:
    data = json.load(data_file)

# Tracklist
tracklist = []
with open('./resources/tracks.txt', 'r') as track_file:
    tracklist = [row.strip() for row in track_file]

CLIENT_ID = data["authentication"]["client_id"]
CLIENT_SECRET = data["authentication"]["client_secret"]
REDIRECT_URI = data["authentication"]["redirect_uri"]
SCOPE = data["authentication"]["scope"]
PLAYLIST_NAME = data["user_data"]["playlist_name"]
USERNAME = data["user_data"]["username"]


# Spotify auth
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri=REDIRECT_URI,
                                               scope=SCOPE))

# Create playlist method
def create_playlist(username, playlist_name, tracklist):
    # Cria a playlist
    playlist = sp.user_playlist_create(user=username, name=playlist_name, public=True)
    playlist_id = playlist['id']
    
    # Pesquisar as músicas e coletar seus URIs
    track_uris = []
    for track in tracklist:
        result = sp.search(q=track, type='track', limit=1)
        if result['tracks']['items']:
            track_uri = result['tracks']['items'][0]['uri']
            track_uris.append(track_uri)
    
    # Adicionar as músicas à playlist
    if track_uris:
        sp.playlist_add_items(playlist_id=playlist_id, items=track_uris)
        print(f"Playlist '{playlist_name}' created!")
    else:
        print("No song found")


# Create playlist!
create_playlist(USERNAME, PLAYLIST_NAME, tracklist)
