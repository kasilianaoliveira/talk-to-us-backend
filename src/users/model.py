import uuid
from typing import TYPE_CHECKING, List, Optional

from sqlalchemy import String
from sqlmodel import Field, Relationship, SQLModel

from src.users.enums import UserRole, UserStatus
from src.utils.models.timestamp_mixin import TimestampMixin

if TYPE_CHECKING:
    from src.tickets.model import Ticket


class User(SQLModel, TimestampMixin, table=True):
    __tablename__ = "users"  # type: ignore
    id: uuid.UUID = Field(
        default_factory=uuid.uuid4, primary_key=True, index=True, nullable=False
    )
    name: str = Field(default=None, index=True, nullable=False, sa_type=String)
    password: Optional[str] = Field(default=None, nullable=True, sa_type=String)
    email: str = Field(index=True, unique=True, nullable=False, sa_type=String)
    role: UserRole = Field(
        default=UserRole.USER,
        nullable=False,
    )
    status: UserStatus = Field(default=UserStatus.PENDING, nullable=False)

    created_tickets: List["Ticket"] = Relationship(
        back_populates="creator",
        sa_relationship_kwargs={"foreign_keys": "[Ticket.creator_id]"},
    )
    assigned_tickets: List["Ticket"] = Relationship(
        back_populates="responsible",
        sa_relationship_kwargs={"foreign_keys": "[Ticket.responsible_id]"},
    )
