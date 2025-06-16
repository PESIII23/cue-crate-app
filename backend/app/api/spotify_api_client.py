from app.services.spotify_auth_service import get_token, get_auth_header
import requests

class SpotifyClient:
    def __init__(self):
        self.token = get_token()
        self.headers = get_auth_header(self.token)

    def search_artist(self, artist_name: str, limit: int = 10):
        url = "https://api.spotify.com/v1/search"
        params = {
            "q": artist_name,
            "type": "artist",
            "limit": limit
        }
        response = requests.get(url, headers=self.headers, params=params)
        response.raise_for_status()
        return response.json()

    def search_track(self, track_name: str, limit: int = 10):
        url = "https://api.spotify.com/v1/search"
        params = {
            "q": track_name,
            "type": "track",
            "limit": limit
        }
        response = requests.get(url, headers=self.headers, params=params)
        response.raise_for_status()
        return response.json()