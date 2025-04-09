# Import all models
# Import all models
from .base import Base, UserType, BookStatus, LoanStatus
from .user import User  # Import User first to avoid circular import issues
from .book import BookAuthorLink, BookCategoryLink, Book  # Import link tables first
from .author import Author
from .category import Category
from .loan import Loan
from .reservation import Reservation

# Fix forward references
User.update_forward_refs()
Book.update_forward_refs()
Author.update_forward_refs()
Loan.update_forward_refs()
Reservation.update_forward_refs()

# List all models for migrations
__all__ = [
    "Base", "UserType", "BookStatus", "LoanStatus",
    "User", "Book", "Author", "Category", "Loan", "Reservation"
]