from sqlmodel import Session

from src.users.schema import UserSchema
from src.users.service import create_user_service


def create_user_controller(user_data: UserSchema, session: Session):
    return create_user_service(user_data=user_data, session=session)
