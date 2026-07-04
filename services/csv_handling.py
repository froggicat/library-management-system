from models.book import Book
import csv
import os

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

def delete_row(inputfile, outputfile, title):
    with open(inputfile, "r", newline="", encoding="utf-8") as infile, open(outputfile, "w", newline="", encoding="utf-8") as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        for row in reader:
            if row[0] != title:
                writer.writerow(row)

    os.replace(outputfile, inputfile)
    