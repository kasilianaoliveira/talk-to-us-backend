import pytest

from src.models.user_model import User
from src.repositories.user_repository import UserRepository


@pytest.mark.asyncio
async def test_create_user(session):
    new_user = User(name="Teste", email="teste@gmail.com", password="12345678")

    repo = UserRepository(session)
    await repo.create(new_user)

    user = await repo.get_user_by_name("Teste")

    assert user is not None, "Usuário não foi encontrado após criação"
    assert user.name == "Teste"


@pytest.mark.asyncio
async def test_delete_user(session):
    new_user = User(
        name="Deletar", email="deletar@example.com", password="senha123"
    )
    repo = UserRepository(session)

    await repo.create(new_user)

    await repo.delete(new_user)

    user = await repo.get_user_by_id(new_user.id)
    assert user is None, "Usuário ainda existe após deleção"


@pytest.mark.asyncio
async def test_get_user_by_email(session):
    new_user = User(
        name="Email", email="email@example.com", password="senha123"
    )
    repo = UserRepository(session)

    await repo.create(new_user)

    user = await repo.get_user_by_email(new_user.email)
    if user:
        assert user.email == "email@example.com"
