from typing import Optional, List, TYPE_CHECKING
from sqlmodel import SQLModel, Field, Relationship

# Handle circular imports
if TYPE_CHECKING:
    from .book import Book, BookAuthorLink  # Import Book and BookAuthorLink for type checking
else:
    from .book import BookAuthorLink  # Import BookAuthorLink for runtime use

class Author(SQLModel, table=True):
    __tablename__ = "authors"

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    
    # Relationship - reference the BookAuthorLink class directly
    books: List["Book"] = Relationship(back_populates="authors", link_model=BookAuthorLink)