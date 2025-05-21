from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    ENVIRONMENT: str = "dev"

    DB_POSTGRES_NAME: str = "task_db"

    DB_POSTGRES_USER: str = "admin"
    DB_POSTGRES_PASSWORD: str = "admin1245"

    TEST_MODE: bool = False

    DB_POSTGRES_HOST: str = "postgres"
    DB_POSTGRES_HOST_LOCAL: str = "localhost"

    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", extra="ignore"
    )

    @property
    def DATABASE_URL_SYNC(self) -> str:
        """Usado pelo Alembic (síncrono)"""
        return (
            f"postgresql+psycopg2://{self.DB_POSTGRES_USER}:"
            f"{self.DB_POSTGRES_PASSWORD}@{self.DB_POSTGRES_HOST_LOCAL}"
            f"/{self.DB_POSTGRES_NAME}"
        )

    @property
    def DATABASE_URL(self) -> str:
        return (
            f"postgresql+asyncpg://{self.DB_POSTGRES_USER}:"
            f"{self.DB_POSTGRES_PASSWORD}@{self.DB_POSTGRES_HOST_LOCAL}"
            f"/{self.DB_POSTGRES_NAME}"
        )
