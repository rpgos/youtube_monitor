import os
from pydantic_settings import BaseSettings, SettingsConfigDict

class Config(BaseSettings):
    # model_config = SettingsConfigDict(env_prefix='my_prefix_')
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    youtube_api_key: str
    telegram_bot_token: str
    telegram_chat_id: str
    check_interval: int = 60 # minutes
    database_url: str = "sqlite:///./youtube.db"
