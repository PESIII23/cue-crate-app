from fastapi import APIRouter, Query
from app.services.spotify import search_artist

router = APIRouter()

@router.get("/search/artist")
def search_artist_route(q: str = Query(...)):
    return search_artist(q)