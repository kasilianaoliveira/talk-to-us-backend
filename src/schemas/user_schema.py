import uuid

from pydantic import BaseModel, EmailStr


class UserSchema(BaseModel):
    name: str
    password: str
    email: EmailStr


class UserPublic(BaseModel):
    id: uuid.UUID
    name: str
    email: EmailStr


class UserPublicBasic(BaseModel):
    id: str
    name: str
