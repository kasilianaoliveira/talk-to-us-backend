from enum import StrEnum


class UserRole(StrEnum):
    USER = "user"
    RESPONSIBLE = "responsible"
    ADMIN = "admin"


class UserStatus(StrEnum):
    PENDING = "pending"
    ACTIVE = "active"
    INACTIVE = "inactive"
