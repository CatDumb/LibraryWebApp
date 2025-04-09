from typing import Optional, TYPE_CHECKING
from datetime import datetime
from sqlmodel import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from .user import User
    from .book import Book

class Reservation(SQLModel, table=True):
    __tablename__ = "reservations"

    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="users.id")
    book_id: int = Field(foreign_key="books.id")
    reservation_date: datetime = Field(default_factory=datetime.now)
    expiry_date: datetime
    is_active: bool = Field(default=True)
    
    # Relationships
    user: "User" = Relationship(back_populates="reservations")
    book: "Book" = Relationship(back_populates="reservations")