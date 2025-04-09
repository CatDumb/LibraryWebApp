from typing import Optional, List, TYPE_CHECKING
from sqlmodel import SQLModel, Field, Relationship

# Handle circular imports
if TYPE_CHECKING:
    from .book import Book, BookCategoryLink
else:
    from .book import BookCategoryLink

class Category(SQLModel, table=True):
    __tablename__ = "categories"

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(unique=True, index=True)
    
    # Relationship - reference the class, not a string
    books: List["Book"] = Relationship(back_populates="categories", link_model=BookCategoryLink)