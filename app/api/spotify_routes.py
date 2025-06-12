from fastapi import APIRouter, Query
from app.services.spotify import search_artist, search_track

router = APIRouter()

@router.get("/search/artist")
def search_artist_route(q: str = Query(...)):
    return search_artist(q)

@router.get("/search/track")
def search_track_route(q: str = Query(...)):
    return search_track(q)