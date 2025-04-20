import uuid

from pydantic import BaseModel, EmailStr


class UserSchema(BaseModel):
    name: str
    password: str
    email: EmailStr


class UserPublic(BaseModel):
    name: str
    email: EmailStr


class UserPublicBasic(BaseModel):
    id: uuid.UUID
    name: str
