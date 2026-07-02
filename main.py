from services.library import Library
from models.book import Book
from models.member import Member
from services.initialise_books import initialise_books

library = Library()
initialise_books(library, "library_books.csv")