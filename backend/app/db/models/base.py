from sqlmodel import SQLModel
from enum import Enum

# Base model
class Base(SQLModel):
    pass

# Core enums
class UserType(str, Enum):
    READER = "reader"
    LIBRARIAN = "librarian"

class BookStatus(str, Enum):
    AVAILABLE = "available"
    CHECKED_OUT = "checked_out"
    RESERVED = "reserved"
    LOST = "lost"

class LoanStatus(str, Enum):
    ACTIVE = "active"
    RETURNED = "returned"
    OVERDUE = "overdue"