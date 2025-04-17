import uuid
from typing import TYPE_CHECKING, Optional

from sqlalchemy import String
from sqlmodel import Field, Relationship, SQLModel

from src.utils.models.timestamp_mixin import TimestampMixin

if TYPE_CHECKING:
    from src.tickets.model import Ticket


class Response(SQLModel, TimestampMixin, table=True):
    __tablename__ = "responses"  # type: ignore

    id: uuid.UUID = Field(
        default_factory=uuid.uuid4, primary_key=True, index=True, nullable=False
    )
    content: str = Field(index=True, nullable=False, sa_type=String)
    ticket_id: uuid.UUID = Field(foreign_key="tickets.id")
    ticket: Optional["Ticket"] = Relationship(back_populates="responses")
