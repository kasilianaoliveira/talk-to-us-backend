import logging
from typing import Annotated

from fastapi import Depends
from sqlmodel import Session, SQLModel, create_engine

from src.infra.core.settings import Settings

logging.basicConfig()
logging.getLogger("sqlalchemy.engine").setLevel(logging.INFO)


setting = Settings()
engine = create_engine(
    setting.DATABASE_URL, pool_pre_ping=True, echo=setting.TEST_MODE == "dev"
)


def create_db_and_tables() -> None:
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]
