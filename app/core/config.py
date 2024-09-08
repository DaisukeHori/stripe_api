from pydantic import BaseSettings
import os

class Settings(BaseSettings):
    PROJECT_NAME: str = "Stripe API FastAPI"
    PROJECT_VERSION: str = "1.0.0"
    STRIPE_API_KEY: str = os.getenv("STRIPE_API_KEY")
    AUTH_KEY: str = os.getenv("AUTH_KEY")  # この行が存在することを確認
    CACHE_TTL: int = 3600
    MAX_LIMIT: int = 100

    class Config:
        env_file = ".env"

settings = Settings()
