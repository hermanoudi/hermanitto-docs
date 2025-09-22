import os
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # Database / auth
    DATABASE_URL: str = os.getenv(
        "DATABASE_URL", "postgresql+asyncpg://user:password@db:5432/db"
    )
    SECRET_KEY: str = os.getenv("SECRET_KEY", "supersecret")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    # Model configuration (app-level feature toggle)
    # Default model used by the application when creating requests to
    # an LLM provider. Setting this only changes which model the app
    # will attempt to use; access still depends on provider perms.
    DEFAULT_MODEL: str = os.getenv("DEFAULT_MODEL", "gpt-5-mini")

    # Comma-separated list in the environment; stored as list[str] here.
    _allowed_models_env = os.getenv("ALLOWED_MODELS", "gpt-5-mini")
    ALLOWED_MODELS: list[str] = [
        m.strip() for m in _allowed_models_env.split(",") if m.strip()
    ]


settings = Settings()
