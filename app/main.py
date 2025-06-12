from fastapi import FastAPI
from dotenv import load_dotenv
import os

app = FastAPI()
load_dotenv()

client_id= os.getenv("SPOTIFY_CLIENT_ID")
client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")

print(client_id, client_secret)

@app.get("/")
async def root():
    return {"message": "CueCrate backend is running!"}
