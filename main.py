from services.library import Library
from models.book import Book
from services.csv_handling import initialise_books

library = Library()
initialise_books(library, "library_books.csv")

library.view_books()