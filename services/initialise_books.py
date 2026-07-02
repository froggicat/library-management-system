from models.book import Book
import csv

def initialise_books(library, file):
    with open(file, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            newBook = Book(row["title"], row["author"])
            library.add_book(newBook)