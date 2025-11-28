from functools import lru_cache
from typing import Literal
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field

class Settings(BaseSettings):
    # pydantic-settings v2 config
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        env_prefix="TITAN_",   # => TITAN_ENV, TITAN_DATABASE_URL, etc.
    )

    app_name: str = "TITAN Threat Intelligence API"
    env: str = "local"
    database_url: str = "sqlite:///./titan.db"

    # REQUIRED: must be present in environment/.env at startup
    jwt_secret: str = Field(...)

    jwt_algorithm: Literal["HS256"] = "HS256"

    access_token_exp_minutes: int = 360
    rate_limit_per_minute: int = 120

@lru_cache
def get_settings() -> Settings:
    return Settings()
