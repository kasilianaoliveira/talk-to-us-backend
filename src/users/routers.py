from http import HTTPStatus

from fastapi import APIRouter, Depends
from sqlmodel import Session

from src.infra.core.connection import get_session
from src.users.controller import create_user_controller
from src.users.schema import UserPublic, UserSchema

user_router = APIRouter(prefix="/users", tags=["Users"])


@user_router.post(
    "", status_code=HTTPStatus.CREATED, response_model=UserPublic
)
def create_user(
    user_data: UserSchema, session: Session = Depends(get_session)
):
    return create_user_controller(user_data, session)
