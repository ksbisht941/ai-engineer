"""
Configuration management using Pydantic Settings.
This file centralizes all environment-based settings.
"""
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    """
    Settings class to hold application configuration.
    It automatically reads values from the .env file.
    """
    DATABASE_URL: str

    class Config:
        env_file = ".env"  # Specifies the environment file to load

# Create a single instance of settings to be used throughout the app
settings = Settings()
