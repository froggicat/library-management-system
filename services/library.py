from services.csv_handling import write_new_row

class Library():
    def __init__(self):
        self.books = []
    
    def add_book(self, book):
        self.books.append(book)
        write_new_row("library_books.csv", book)


    def view_books(self):
        if not self.books:
            print("There are no books in the library at this time.")
            return
        for book in self.books:
            print(book)

