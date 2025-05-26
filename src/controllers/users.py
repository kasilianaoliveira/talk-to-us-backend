from http import HTTPStatus
from uuid import UUID

from fastapi import APIRouter, Depends

from src.schemas.responses_messages import (
    MessageResponse,
    StandardSuccessResponse,
)
from src.schemas.user_schema import (
    UserCreateDTO,
    UserResponseDTO,
)
from src.services.user_service import UserService, get_user_service

user_router = APIRouter(prefix="/users", tags=["Users"])


@user_router.post(
    "/",
    status_code=HTTPStatus.CREATED,
    response_model=StandardSuccessResponse,
)
async def create_new_user(
    user_data: UserCreateDTO,
    user_service: UserService = Depends(get_user_service),
):
    created_user = await user_service.create_user(user_data)
    return StandardSuccessResponse(
        message="Usuário criado com sucesso!",
        data=created_user,
    )


@user_router.get(
    "/{user_id}",
    status_code=HTTPStatus.CREATED,
    response_model=UserResponseDTO,
)
async def get_user(
    user_id: UUID, user_service: UserService = Depends(get_user_service)
):
    return await user_service.get_user(user_id)


@user_router.delete(
    "/{user_id}",
    status_code=HTTPStatus.CREATED,
    response_model=MessageResponse,
)
async def delete_user(
    user_id: UUID,
    user_service: UserService = Depends(get_user_service),
):
    return await user_service.delete_user(user_id)
