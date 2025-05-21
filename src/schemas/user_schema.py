import uuid
from typing import Optional

from pydantic import BaseModel, ConfigDict, EmailStr


class UserCreateDTO(BaseModel):
    name: str
    password: str
    email: EmailStr


class UserUpdateDTO(BaseModel):
    name: Optional[str] = None
    password: Optional[str] = None
    email: Optional[EmailStr] = None


class UserResponseDTO(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    name: str
    email: EmailStr
