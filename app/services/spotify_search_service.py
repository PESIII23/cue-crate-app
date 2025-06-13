from app.utils.spotify_api_client import SpotifyClient

def search_artist(artist_name, limit=10):
    client = SpotifyClient()
    return client.search_artist(artist_name, limit)

def search_track(track_name, limit=10):
    client = SpotifyClient()
    return client.search_track(track_name, limit)