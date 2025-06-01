import os

from fastapi import FastAPI
from dotenv import load_dotenv
import requests

app = FastAPI()
load_dotenv()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/trending")
async def trending():
    token = os.getenv("TMDB_READ_ACCESS_TOKEN")
    if not token:
        return {"error": "TMDB_READ_TOKEN not set"}

    url = "https://api.themoviedb.org/3/trending/all/week?language=en-US"

    print("Value of 'bearer token' environmental variable: ", token)

    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {token}"
    }

    response = requests.get(url, headers=headers)

    try:
        return response.json()
    except Exception as e:
        return {"error": "Failed to parse response", "raw": str(e)}