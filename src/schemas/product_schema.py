import uuid
from datetime import datetime
from decimal import Decimal
from typing import List, Optional

from pydantic import BaseModel, ConfigDict, ValidationInfo, field_validator

from src.models.enums import ProductStatus


class ProductInput(BaseModel):
    name: str
    stock: int
    unit_price: Decimal
    status: ProductStatus = ProductStatus.IN_STOCK
    user_id: uuid.UUID

    @field_validator("unit_price")
    def validate_price(cls, value: Decimal) -> Decimal:
        if value <= 0:
            raise ValueError("Invalid price")
        return value


class ProductOutput(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: uuid.UUID
    name: str
    stock: int
    unit_price: Decimal
    status: ProductStatus
    user_id: uuid.UUID
    created_at: datetime
    updated_at: datetime


class PaginatedProductResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    items: List[ProductOutput]
    total: int
    page: int
    limit: int
    pages: int
    has_next: bool
    has_prev: bool


class ProductUpdate(BaseModel):
    name: Optional[str] = None
    stock: Optional[int] = None
    unit_price: Optional[Decimal] = None
    status: Optional[ProductStatus] = None

    @field_validator("unit_price")
    def validate_price(cls, value: Optional[Decimal]) -> Optional[Decimal]:
        if value is not None and value <= 0:
            raise ValueError("Invalide price")
        return value

    @field_validator("stock")
    def validate_stock_status(
        cls, value: Optional[int], info: ValidationInfo
    ) -> Optional[int]:
        values = info.data
        status = values.get("status")
        if value is not None:
            if value > 0 and status == ProductStatus.SOLD_OUT:
                raise ValueError(
                    "Stock cannot be greater than 0 if status is OUT_OF_STOCK"
                )
            elif value == 0 and status == ProductStatus.IN_STOCK:
                raise ValueError("Stock cannot be 0 if status is IN_STOCK")
        return value

    @field_validator("status")
    def validate_status_stock(
        cls, value: Optional[ProductStatus], info: ValidationInfo
    ) -> Optional[ProductStatus]:
        values = info.data
        stock = values.get("stock")
        if value == ProductStatus.IN_STOCK and stock == 0:
            raise ValueError("Status cannot be IN_STOCK if stock is 0")
        elif (
            value == ProductStatus.SOLD_OUT and stock is not None and stock > 0
        ):
            raise ValueError(
                "Status cannot be OUT_OF_STOCK if stock is greater than 0",
            )
        return value
