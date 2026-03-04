from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache


class Settings(BaseSettings):
    # Database
    database_url: str

    # Mailchimp
    mailchimp_api_key: str = ""
    mailchimp_list_id: str = ""
    mailchimp_dc: str = "us21"

    # Contact form
    contact_recipient_email: str = ""

    # App
    allowed_origins: str = "http://localhost:5500"
    app_env: str = "development"
    secret_key: str = "dev-secret-key"

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    @property
    def origins_list(self) -> list[str]:
        return [o.strip() for o in self.allowed_origins.split(",")]

    @property
    def is_production(self) -> bool:
        return self.app_env == "production"


@lru_cache
def get_settings() -> Settings:
    return Settings()
