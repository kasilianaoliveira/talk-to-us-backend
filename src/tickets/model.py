import uuid
from typing import TYPE_CHECKING, List, Optional

from sqlalchemy import String
from sqlmodel import Field, Relationship, SQLModel

from src.tickets.enums import TicketPriority, TicketStatus
from src.utils.models.timestamp_mixin import TimestampMixin

if TYPE_CHECKING:
    from src.responses.model import Response
    from src.users.model import User


class Ticket(SQLModel, TimestampMixin, table=True):
    __tablename__ = "tickets"  # type: ignore

    id: uuid.UUID = Field(
        default_factory=uuid.uuid4, primary_key=True, index=True, nullable=False
    )
    title: str = Field(index=True, nullable=False, sa_type=String)
    description: str = Field(index=True, nullable=False, sa_type=String)
    priority: TicketPriority = Field(
        default=TicketPriority.LOW,
        nullable=False,
    )
    status: TicketStatus = Field(default=TicketStatus.OPEN)

    creator_id: uuid.UUID = Field(foreign_key="users.id")
    creator: "User" = Relationship(back_populates="created_tickets")

    responsible_id: Optional[uuid.UUID] = Field(default=None, foreign_key="users.id")
    responsible: Optional["User"] = Relationship(back_populates="assigned_tickets")

    responses: List["Response"] = Relationship(back_populates="ticket")
