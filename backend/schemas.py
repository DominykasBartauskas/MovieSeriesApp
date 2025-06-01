from typing import List, Literal, Optional

from pydantic import BaseModel, Field, root_validator


class TrendingItem(BaseModel):
    id: int
    title: str
    overview: str
    poster_path: Optional[str] = None
    media_type: Literal["movie", "tv"]
    original_title: Optional[str] = None
    original_language: Optional[str] = None
    release_date: str
    vote_average: Optional[float] = None
    vote_count: Optional[int] = None
    genres: List[int] = Field(default_factory=list, alias="genre_ids")

    @root_validator(pre=True)
    def normalize_fields(cls, values):
        media_type = values.get("media_type")
        if media_type == "tv":
            if "name" in values:
                values["title"] = values["name"]
            if "original_name" in values:
                values["original_title"] = values["original_name"]
            if "first_air_date" in values:
                values["release_date"] = values["first_air_date"]
        return values

    class Config:
        allow_population_by_field_name = True
        extra = "ignore"


class TrendingResponse(BaseModel):
    page: int
    results: List[TrendingItem]

    class Config:
        extra = "ignore"
