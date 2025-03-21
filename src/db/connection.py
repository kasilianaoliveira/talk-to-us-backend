from decouple import config
from sqlmodel import Session, create_engine

DB_URL = config("DB_URL", cast=str)

if not isinstance(DB_URL, str):
    raise TypeError("DB_URL must be a string.")

engine = create_engine(DB_URL, pool_pre_ping=True)


def get_session():
    with Session(engine) as session:
        yield session
