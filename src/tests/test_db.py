import pytest
from sqlmodel import select

from src.models.user_model import User


@pytest.mark.asyncio
async def test_create_user(session):
    new_user = User(name="Teste", email="teste@gmail.com", password="12345678")

    session.add(new_user)
    await session.commit()

    user = await session.scalar(select(User).where(User.name == "Teste"))
    assert user.name == "Teste"
