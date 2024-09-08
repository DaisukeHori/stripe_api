from pydantic import BaseSettings
import os

class Settings(BaseSettings):
    PROJECT_NAME: str = "Stripe API FastAPI"
    PROJECT_VERSION: str = "1.0.0"
    STRIPE_API_KEY: str = os.getenv("STRIPE_API_KEY")
    CACHE_TTL: int = 3600  # 1 hour
    MAX_LIMIT: int = 100

    class Config:
        env_file = ".env"

settings = Settings()