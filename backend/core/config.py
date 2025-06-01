from pydantic import BaseSettings

class Settings(BaseSettings):
    TMDB_READ_ACCESS_TOKEN: str
    TMDB_API_KEY: str
    TMDB_BASE_URL: str = "https://api.themoviedb.org/3"

    class Config:
        env_file = ".env"

settings = Settings()