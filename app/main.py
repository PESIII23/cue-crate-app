from fastapi import FastAPI
from dotenv import load_dotenv
from app.api.spotify_routes import router as spotify_router

app = FastAPI()
load_dotenv()

app.include_router(spotify_router, prefix="/spotify")

@app.get("/")
async def root():
    return {"message": "CueCrate backend is running!"}
