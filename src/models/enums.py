from enum import Enum


class UserType(str, Enum):
    ADMIN = "Admin"
    RESPONSIBLE = "Responsible"
    DEFAULT = "Default"
