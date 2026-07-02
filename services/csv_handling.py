from models.book import Book
import csv

def initialise_books(library, file):
    with open(file, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            newBook = Book(row["title"], row["author"])
            library.books.append(newBook)

def write_new_row(file, book):
    with open(file, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([book.title, book.author])