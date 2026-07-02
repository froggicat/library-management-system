class Library():
    def __init__(self):
        self.books = []
        self.members = []

    def add_member(self, member):
        self.members.append(member)

    def view_members(self):
        for member in self.members:
            print(member)
    
    def add_book(self, book):
        self.books.append(book)

    def view_books(self):
        if not self.books:
            print("There are no books in the library at this time.")
            return
        for book in self.books:
            print(book)

    def borrow_book(self, book, member):
        if book.isavailable == False:
            print("Cannot borrow this book at the moment.")
        else:
            member.borrowed_books.append(book)
            book.isavailable = False
            print("Book borrowed!")
