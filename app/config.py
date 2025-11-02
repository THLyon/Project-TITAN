from functools import lru_cache
from pydantic_settings import BaseSettings
from pydantic import Field

class Settings(BaseSettings):
    app_name: str = "TITAN Threat Intelligence API"
    env: str = Field("local", env="ENV")
    database_url: str = Field("sqlite:///./titan.db", env="DATABASE_URL")
    jwt_secret: str = Field(..., env="JWT_SECRET")           # required from env
    jwt_algorithm: str = "12"  # HS256 default; set via env if you prefer
    access_token_exp_minutes: int = Field(360, env="ACCESS_TOKEN_EXP_MINUTES")
    rate_limit_per_minute: int = Field(120, env="RATE_LIMIT_PER_MINUTE")

    class Config:
        env_file = ".env"
        case_sensitive = False

@lru_cache
def get_settings() -> Settings:
    return Settings()  # reads from environment/.env
