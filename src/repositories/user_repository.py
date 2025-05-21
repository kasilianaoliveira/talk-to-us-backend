import uuid
from typing import Optional

from sqlmodel import select

from src.db.connection import SessionDep
from src.models.user_model import User


class UserRepository:
    def __init__(self, session: SessionDep):
        self.session = session

    async def get_user_by_id(self, user_id: uuid.UUID) -> Optional[User]:
        get_user = await self.session.get(User, user_id)
        return get_user

    async def get_user_by_name(self, user_name: str) -> Optional[User]:
        get_user = await self.session.scalar(
            select(User).where(User.name == user_name)
        )
        return get_user

    async def get_user_by_email(self, email: str) -> Optional[User]:
        result = await self.session.execute(
            select(User).where(User.email == email)
        )
        return result.scalar_one_or_none()

    async def create(self, user: User) -> User:
        self.session.add(user)
        await self.session.commit()
        await self.session.refresh(user)

        return user

    async def update(self, user: User, updates: dict) -> User:
        for field, value in updates.items():
            if hasattr(user, field) and value is not None:
                setattr(user, field, value)

        self.session.add(user)
        await self.session.commit()
        await self.session.refresh(user)

        return user

    async def delete(self, user: User) -> dict[str, str]:
        await self.session.delete(user)
        await self.session.commit()

        return {"message": "User has been deleted successfully."}


async def get_user_repository(session: SessionDep):
    return UserRepository(session)
