import uuid
from decimal import Decimal
from typing import TYPE_CHECKING, Optional

from sqlalchemy import Column, Numeric, String
from sqlmodel import Field, Relationship, SQLModel

from src.models.enums import ProductStatus
from src.utils.models.timestamp_mixin import TimestampMixin

if TYPE_CHECKING:
    from src.models.user_model import User


class Product(SQLModel, TimestampMixin, table=True):
    __tablename__ = "products"  # type: ignore
    id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        primary_key=True,
        index=True,
        nullable=False,
    )
    name: str = Field(
        default=None, unique=True, index=True, nullable=False, sa_type=String
    )
    description: str = Field(default=None, nullable=True, sa_type=String)
    stock: int
    unit_price: Decimal = Field(
        sa_column=Column(Numeric(10, 2), nullable=False, default=0.00)
    )
    status: ProductStatus = Field(
        default=ProductStatus.IN_STOCK, nullable=False, index=True
    )

    user_id: uuid.UUID = Field(foreign_key="users.id")
    owner: Optional["User"] = Relationship(back_populates="products")
