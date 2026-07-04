from services.library import Library
from models.book import Book
from services.csv_handling import initialise_books

library = Library()
initialise_books(library, "library_books.csv")

def main():
    while True:
        print("Welcome to Lia's Library!")
        print("1. View Books")
        print("2. Add a book")
        print("3. Remove a book")
        print("4. Exit library")

        user_choice = int(input("What would you like to do? (input a number!)"))
        if user_choice == 1:
            library.view_books()
        elif user_choice == 2:
            new_title = input("New book's title: ")
            new_author = input("New book's author: ")
            new_book = Book(new_title, new_author)
            library.add_book(new_book)
        elif user_choice == 3:
            title_to_remove = input("Title of book to be removed: ")
            library.remove_book(title_to_remove)
        elif user_choice == 4:
            break
        else:
            print("Invalid option - please input one of the numbers above!")

main()