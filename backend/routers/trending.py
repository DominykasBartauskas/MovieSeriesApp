import os

import requests
from dotenv import load_dotenv
from fastapi import APIRouter, HTTPException

from backend.schemas import TrendingResponse

router = APIRouter()
load_dotenv()


@router.get("/trending", response_model=TrendingResponse)
async def get_trending():
    token = os.getenv("TMDB_READ_ACCESS_TOKEN")
    if not token:
        raise HTTPException(status_code=500, detail="TMDB_READ_ACCESS_TOKEN not set")

    url = "https://api.themoviedb.org/3/trending/all/week?language=en-US"

    headers = {"accept": "application/json", "Authorization": f"Bearer {token}"}

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        raise HTTPException(
            status_code=response.status_code, detail="Failed to fetch trending data"
        )

    data = response.json()

    try:
        validated = TrendingResponse(**data)
        return validated
    except Exception as e:
        return HTTPException(status_code=500, detail=f"Validation error: {e}")
