from app.services.spotify_auth import get_token, get_auth_header
from requests import get
import json

def search_artist(artist_name, limit=1):
    token = get_token()
    headers = get_auth_header(token)
    url = "https://api.spotify.com/v1/search"
    params = {"q": artist_name, "type": "artist", "limit": limit}
    result = get(url, headers=headers, params=params)
    return result.json()

print(search_artist("ACDC"))