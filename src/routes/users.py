from http import HTTPStatus

from fastapi import APIRouter, Depends

from src.schemas.user_schema import UserPublic, UserSchema
from src.services.user_service import UserService, get_user_service

user_router = APIRouter(prefix="/users", tags=["Users"])


@user_router.post(
    "/create",
    status_code=HTTPStatus.CREATED,
    response_model=UserPublic,
)
async def create_new_user(
    user_in: UserSchema, user_service: UserService = Depends(get_user_service)
):
    return await user_service.create_user(user_in)
