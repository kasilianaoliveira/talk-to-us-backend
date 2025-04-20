from http import HTTPStatus

from fastapi import HTTPException
from sqlmodel import Session, select

from src.infra.core.security import hash_password
from src.users.model import User
from src.users.schema import UserSchema


def create_user_service(user_data: UserSchema, session: Session):
    existing_user = session.exec(
        select(User).where(User.email == user_data.email)
    ).first()

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

    session.add(user)
    session.commit()
    session.refresh(user)
    return user


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
