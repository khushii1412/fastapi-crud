from pydantic_settings import BaseSettings  # ✅ New (correct for Pydantic v2+)

class Settings(BaseSettings):
    database_url: str

    class Config:
        env_file = ".env"

settings = Settings()
