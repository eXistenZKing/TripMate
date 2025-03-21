from pathlib import Path
from pydantic_settings import BaseSettings


BASE_DIR = Path(__file__).resolve().parent.parent.parent
ENV_FILE = BASE_DIR / ".env"


class Setting(BaseSettings):
    DB_HOST: str = "localhost"
    DB_PORT: int = 5432
    DB_USER: str = "postgres"
    DB_PASS: str = "postgres"
    DB_NAME: str = "postgres"

    PYTHONPATH: str = "backend/src"

    db_url: str = f"sqlite+aiosqlite:///{BASE_DIR}/db.sqlite3"
    # db_url: str = (f"postgresql+asyncpg://{DB_USER}:{DB_PASS}"
    #                f"@{DB_HOST}:{DB_PORT}/{DB_NAME}")

    class Config:
        env_file = ENV_FILE


settings = Setting()
