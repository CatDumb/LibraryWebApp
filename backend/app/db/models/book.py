from typing import Optional, List, TYPE_CHECKING
from datetime import datetime
from sqlmodel import SQLModel, Field, Relationship, Column, Text

from .base import BookStatus

# Handle circular imports
if TYPE_CHECKING:
    from .author import Author
    from .category import Category
    from .loan import Loan
    from .reservation import Reservation

# Association tables
class BookAuthorLink(SQLModel, table=True):
    book_id: Optional[int] = Field(default=None, foreign_key="books.id", primary_key=True)
    author_id: Optional[int] = Field(default=None, foreign_key="authors.id", primary_key=True)

class BookCategoryLink(SQLModel, table=True):
    book_id: Optional[int] = Field(default=None, foreign_key="books.id", primary_key=True)
    category_id: Optional[int] = Field(default=None, foreign_key="categories.id", primary_key=True)

class Book(SQLModel, table=True):
    __tablename__ = "books"

    id: Optional[int] = Field(default=None, primary_key=True)
    isbn: str = Field(unique=True, index=True)
    title: str = Field(index=True)
    description: Optional[str] = Field(default=None, sa_column=Column(Text))
    publication_year: Optional[int] = None
    publisher: Optional[str] = None
    total_copies: int = Field(default=1)
    available_copies: int = Field(default=1)
    status: BookStatus = Field(default=BookStatus.AVAILABLE)
    date_added: datetime = Field(default_factory=datetime.now)

    # Relationships
    authors: List["Author"] = Relationship(back_populates="books", link_model=BookAuthorLink)
    categories: List["Category"] = Relationship(back_populates="books", link_model=BookCategoryLink)
    loans: List["Loan"] = Relationship(back_populates="book")
    reservations: List["Reservation"] = Relationship(back_populates="book")