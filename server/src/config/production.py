from .config import Settings
from pydantic_settings import SettingsConfigDict

class ProductionSettings(Settings):
    DEBUG: bool = False
    LOG_LEVEL: str = "INFO"
    
    model_config = SettingsConfigDict(
        env_file=(".env", ".env.production"),
        env_file_encoding="utf-8",
        extra="ignore"
    )

prod_settings = ProductionSettings()
