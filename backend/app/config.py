"""
Application Configuration
=========================
Owner: Ritik Budhathoki

Loads all settings from the .env file using pydantic-settings.
Access anywhere in the app via: from app.config import settings

TODO (Ritik):
    - Add any additional config fields as development progresses
"""

from pydantic_settings import BaseSettings
from typing import List


class Settings(BaseSettings):
    """Application settings loaded from environment variables / .env file."""

    # Application
    APP_NAME: str = "Secure-Plants_Diagnosis"
    APP_VERSION: str = "0.1.0"
    APP_ENV: str = "development"
    DEBUG: bool = True

    # Server
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    ALLOWED_ORIGINS: List[str] = ["http://localhost:3000"]

    # Database
    DB_HOST: str = "localhost"
    DB_PORT: int = 5432
    DB_NAME: str = "plant_diagnosis_db"
    DB_USER: str = "postgres"
    DB_PASSWORD: str = ""
    DATABASE_URL: str = ""

    # JWT
    JWT_SECRET_KEY: str = ""
    JWT_ALGORITHM: str = "HS256"
    JWT_ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    JWT_REFRESH_TOKEN_EXPIRE_DAYS: int = 7

    # Security
    MAX_UPLOAD_SIZE_MB: int = 5
    ALLOWED_IMAGE_TYPES: List[str] = ["image/jpeg", "image/png", "image/jpg"]
    RATE_LIMIT_REQUESTS: int = 100
    RATE_LIMIT_WINDOW_SECONDS: int = 60

    # ML Model
    MODEL_PATH: str = "models/student/deit_tiny_plant_diagnosis.pth"
    MODEL_INPUT_SIZE: int = 224
    MODEL_NUM_CLASSES: int = 15
    INFERENCE_DEVICE: str = "cpu"

    # Logging
    LOG_LEVEL: str = "INFO"
    LOG_FILE: str = "logs/app.log"

    class Config:
        env_file = ".env"
        case_sensitive = True


# Global settings instance — import this throughout the app
settings = Settings()
