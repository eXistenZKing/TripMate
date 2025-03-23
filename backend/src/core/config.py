from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).resolve().parent.parent.parent


class AuthSettings(BaseSettings):
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int

    model_config = SettingsConfigDict(
        env_file=(BASE_DIR / ".env.example", BASE_DIR / ".env"),
        extra="ignore"
    )


class Settings(BaseSettings):
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str

    auth: AuthSettings = AuthSettings()

    @property
    def db_url(self) -> str:
        return (f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}"
                f"@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}")

    model_config = SettingsConfigDict(
        env_file=(BASE_DIR / ".env.example", BASE_DIR / ".env"),
        extra="ignore"
    )


settings = Settings()
