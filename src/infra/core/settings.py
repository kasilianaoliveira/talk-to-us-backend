from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    ENVIRONMENT: str = "dev"

    POSTGRES_DB: str = "main"
    POSTGRES_USER: str = "admin"
    POSTGRES_PASSWORD: str = "admin1245"
    TEST_MODE: bool = False
    POSTGRES_HOST: str = "postgresql"
    # POSTGRES_HOST_TEST: str = "postgresql-test"
    POSTGRES_HOST_LOCAL: str = "localhost"

    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", extra="ignore"
    )

    @property
    def DATABASE_URL_SYNC(self) -> str:
        # db_host = self.POSTGRES_HOST_TEST
        # if self.TEST_MODE else self.POSTGRES_HOST
        return (
            f"postgresql+psycopg2://{self.POSTGRES_USER}:"
            f"{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST_LOCAL}"
            f"/{self.POSTGRES_DB}"
        )

    @property
    def DATABASE_URL(self) -> str:
        # db_host = self.POSTGRES_HOST_TEST
        # if self.TEST_MODE else self.POSTGRES_HOST
        return (
            f"postgresql+asyncpg://{self.POSTGRES_USER}:"
            f"{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST_LOCAL}"
            f"/{self.POSTGRES_DB}"
        )
