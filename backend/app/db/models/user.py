from typing import Optional, List, TYPE_CHECKING
from datetime import datetime
from sqlmodel import SQLModel, Field, Relationship

from .base import UserType

# Handle circular imports
if TYPE_CHECKING:
    from .loan import Loan
    from .reservation import Reservation

class User(SQLModel, table=True):
    __tablename__ = "users"

    id: Optional[int] = Field(default=None, primary_key=True)
    username: str = Field(unique=True, index=True)
    password: str
    email: str = Field(unique=True, index=True)
    name: str
    user_type: UserType
    phone: Optional[str] = None
    registration_date: datetime = Field(default_factory=datetime.now)
    
    # Relationships
    loans: List["Loan"] = Relationship(back_populates="user")
    reservations: List["Reservation"] = Relationship(back_populates="user")