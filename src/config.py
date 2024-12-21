"""Configuration settings for the prompt generation service."""

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    openai_api_key: str
    mongodb_uri: str
    model_name: str = "gpt-4"

    class Config:
        """Pydantic configuration for environment variable loading."""

        env_file = ".env"


settings = Settings()
