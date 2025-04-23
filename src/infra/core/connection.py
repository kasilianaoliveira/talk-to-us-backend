import logging
from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from src.infra.core.settings import Settings


logging.basicConfig()
logging.getLogger("sqlalchemy.engine").setLevel(logging.INFO)


setting = Settings()
engine = create_async_engine(
    setting.DATABASE_URL, pool_pre_ping=True, echo=setting.TEST_MODE == "dev"
)


async def get_session():
    async with AsyncSession(engine) as session:
        yield session


SessionDep = Annotated[AsyncSession, Depends(get_session)]
