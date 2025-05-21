from http import HTTPStatus
from typing import Annotated
from uuid import UUID

from fastapi import Depends, HTTPException

from src.db.security import hash_password
from src.models.user_model import User
from src.repositories.user_repository import (
    UserRepository,
    get_user_repository,
)
from src.schemas.user_schema import UserCreateDTO


class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    async def get_user(self, user_id: UUID) -> User:
        existing_user = await self.user_repository.get_user_by_id(
            user_id,
        )

        if not existing_user:
            raise HTTPException(
                status_code=HTTPStatus.BAD_REQUEST,
                detail="User does not exist.",
            )

        return existing_user

    async def create_user(self, user_data: UserCreateDTO) -> User:
        existing_user = await self.user_repository.get_user_by_email(
            user_data.email,
        )

        if existing_user:
            raise HTTPException(
                status_code=HTTPStatus.BAD_REQUEST,
                detail="Email already registered.",
            )

        user = User(
            name=user_data.name,
            email=user_data.email,
            password=hash_password(user_data.password),
        )
        result_user = await self.user_repository.create(user)
        return result_user

    async def delete_user(self, user_id) -> dict[str, str]:
        existing_user = await self.user_repository.get_user_by_id(user_id)

        if not existing_user:
            raise HTTPException(
                status_code=HTTPStatus.BAD_REQUEST,
                detail="User does not exist.",
            )

        return await self.user_repository.delete(existing_user)


async def get_user_service(
    user_repository: Annotated[UserRepository, Depends(get_user_repository)],
):
    return UserService(user_repository)


# def list_user_service(user_data: UserPublic, session: Session):

#     user = User(
#         name=user_data.name,
#         email=user_data.email,
#         role=user_data.role,
#         status=user_data.status,
#         password=hash_password(user_data.password),
#     )

#     session.add(user)
#     session.commit()
#     session.refresh(user)
#     return user
