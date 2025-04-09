from typing import Optional, TYPE_CHECKING
from datetime import datetime
from sqlmodel import SQLModel, Field, Relationship

from .base import LoanStatus

if TYPE_CHECKING:
    from .user import User
    from .book import Book

class Loan(SQLModel, table=True):
    __tablename__ = "loans"

    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="users.id")
    book_id: int = Field(foreign_key="books.id")
    checkout_date: datetime = Field(default_factory=datetime.now)
    due_date: datetime
    return_date: Optional[datetime] = None
    status: LoanStatus = Field(default=LoanStatus.ACTIVE)
    
    # Relationships
    user: "User" = Relationship(back_populates="loans")
    book: "Book" = Relationship(back_populates="loans")