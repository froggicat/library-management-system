from services.library import Library
from models.book import Book
from models.member import Member
import csv

library = Library()

with open("library_books.csv", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        newBook = Book(row["title"], row["author"])
        library.add_book(newBook)