import os
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import SecretStr

class Settings(BaseSettings):
    BOT_API_KEY: SecretStr
    DATABASE_URL: str = "sqlite+aiosqlite:///./db.sqlite3"
    ECHO_SQL: bool = False

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )

settings = Settings()
