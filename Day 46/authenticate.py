import spotipy
from spotipy.oauth2 import SpotifyOAuth
from decouple import config

spotify = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=config("SPOTIFY_ID"),
        client_secret=config("SPOTIFY_CLIENT_SECRET"),
        show_dialog=True,
        cache_path="Day 46/token.txt",
        username=config("SPOTIFY_USERNAME"), 
    )
)
