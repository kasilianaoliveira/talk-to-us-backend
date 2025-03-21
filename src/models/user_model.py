import uuid
from typing import Optional
from uuid import UUID

from pydantic import EmailStr
from sqlmodel import Field, Relationship, SQLModel

from src.models.enums import UserType
from src.models.ticket_model import Ticket


class User(SQLModel, table=True):
    id: UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    name: str = Field(index=True)
    email: EmailStr = Field(unique=True)
    phone: Optional[str] = None
    user_type: UserType = Field(default=UserType.DEFAULT)


tickets_opened: list[Ticket] = Relationship(back_populates="requester")
tickets_responsible: list[Ticket] = Relationship(back_populates="responsible")
