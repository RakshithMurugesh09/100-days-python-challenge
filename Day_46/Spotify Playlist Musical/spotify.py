import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from main import song_names
from dotenv import load_dotenv
import os

load_dotenv('spotify.env')

spotify = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id=os.getenv("SPOTIPY_CLIENT_ID"),
    client_secret=os.getenv("SPOTIPY_CLIENT_SECRET")
))

for song in song_names[:1]:
    song_name = song.get_text(strip=True)
    result = spotify.search(q='song:' + song_name, type='track', limit=1)
    tracks = result["tracks"]["items"]

    if tracks:
        track = tracks[0]

        print(f"Search: {song_name}")
        print(f"Found: {track['name']}")
        print(f"Artist: {track['artists'][0]['name']}")
        print(f"Spotify URI: {track['uri']}")
        print(f"Spotify URL: {track['external_urls']['spotify']}")
        print("-" * 40)

    else:
        print(f"Song not found: {song}")

