from .config import Settings
from pydantic_settings import SettingsConfigDict

class DevelopmentSettings(Settings):
    DEBUG: bool
    LOG_LEVEL: str = "DEBUG"
    
    model_config = SettingsConfigDict(
        env_file=(".env", ".env.development"),
        env_file_encoding="utf-8",
        extra="ignore"
    )

dev_settings = DevelopmentSettings()
