import uuid
from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel, ConfigDict, field_validator

from src.models.enums import ProductStatus


class ProductCreateDTO(BaseModel):
    name: str
    description: str
    stock: int
    unit_price: Decimal
    status: ProductStatus = ProductStatus.IN_STOCK
    user_id: str

    @field_validator("unit_price")
    def validate_price(cls, value: Decimal) -> Decimal:
        if value <= 0:
            raise ValueError("Invalid price")
        return value


class ProductResponseDTO(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: uuid.UUID
    name: str
    description: str
    stock: int
    unit_price: Decimal
    status: ProductStatus
    user_id: uuid.UUID
    created_at: datetime
    updated_at: datetime
