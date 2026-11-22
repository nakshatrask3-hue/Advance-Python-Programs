
class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = True


class Patron:
    def __init__(self, patron_id, name):
        self.patron_id = patron_id
        self.name = name
        self.borrowed_books = []


class Library:
    def __init__(self):
        self.books = []
        self.patrons = []

    def add_book(self, book):
        self.books.append(book)
        print("Book added successfully!")

    def register_patron(self, patron):
        self.patrons.append(patron)
        print("Patron registered successfully!")

    def borrow_book(self, book_id, patron_id):
        for book in self.books:
            if book.book_id == book_id and book.available:
                for patron in self.patrons:
                    if patron.patron_id == patron_id:
                        book.available = False
                        patron.borrowed_books.append(book)
                        print("Book borrowed successfully!")
                        return
                print("Patron not found!")
                return
        print("Book not available!")

    def return_book(self, book_id, patron_id):
        for patron in self.patrons:
            if patron.patron_id == patron_id:
                for book in patron.borrowed_books:
                    if book.book_id == book_id:
                        book.available = True
                        patron.borrowed_books.remove(book)
                        print("Book returned successfully!")
                        return
                print("Book not borrowed by this patron!")
                return
        print("Patron not found!")

    def display_books(self):
        print("\nLibrary Books:")
        for book in self.books:
            status = "Available" if book.available else "Borrowed"
            print(book.book_id, book.title, book.author, status)


# Main Program
library = Library()

# Adding books
library.add_book(Book(1, "Python Programming", "Guido"))
library.add_book(Book(2, "Data Structures", "Mark Allen"))

# Registering patrons
library.register_patron(Patron(101, "Rahul"))
library.register_patron(Patron(102, "Priya"))

# Display books
library.display_books()

# Borrowing a book
library.borrow_book(1, 101)

# Display books after borrowing
library.display_books()

# Returning a book
library.return_book(1, 101)

# Display books after returning
library.display_books()
