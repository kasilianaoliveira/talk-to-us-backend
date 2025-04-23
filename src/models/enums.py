from enum import StrEnum


class UserRole(StrEnum):
    USER = "user"
    RESPONSIBLE = "responsible"
    ADMIN = "admin"


class UserStatus(StrEnum):
    PENDING = "pending"
    ACTIVE = "active"
    INACTIVE = "inactive"


class ProductStatus(StrEnum):
    IN_STOCK = "in_stock"
    SOLD_OUT = "sold_out"
