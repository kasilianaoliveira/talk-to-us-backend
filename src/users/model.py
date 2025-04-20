import uuid
from typing import List, Optional

from pydantic import EmailStr
from sqlalchemy import String
from sqlmodel import Field, Relationship, SQLModel

# if TYPE_CHECKING:
from src.products.model import Product
from src.utils.models.timestamp_mixin import TimestampMixin


class User(SQLModel, TimestampMixin, table=True):
    __tablename__ = "users"  # type: ignore
    id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        primary_key=True,
        index=True,
        nullable=False,
    )
    name: str = Field(default=None, index=True, nullable=False, sa_type=String)
    password: Optional[str] = Field(
        default=None, nullable=True, sa_type=String
    )
    email: EmailStr = Field(
        index=True, unique=True, nullable=False, sa_type=String
    )
    products: List["Product"] = Relationship(
        back_populates="user", cascade_delete=True
    )
