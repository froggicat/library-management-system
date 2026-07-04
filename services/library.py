from services.csv_handling import write_new_row, delete_row

class Library():
    def __init__(self):
        self.books = []
    
    def add_book(self, newBook):
        self.books.append(newBook)
        write_new_row("library_books.csv", newBook)


    def view_books(self):
        if not self.books:
            print("There are no books in the library at this time.")
            return
        for book in self.books:
            print(book)

    def remove_book(self, title):
        #removing a book from the library's own list
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
        
        #removing a row from the csv
        delete_row("library_books.csv", "temp.csv", title)
