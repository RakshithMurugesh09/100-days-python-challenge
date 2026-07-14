from book import Book


class Library:

    def __init__(self):
        self.books = []

    def add_book(self):
        book = Book()
        self.books.append(book)

        print(f"\n'{book.title}' added successfully.")

    def view_books(self):

        if not self.books:
            print("No books available.")
            return

        for book in self.books:
            book.display_details()

    def find_book(self, title):

        for book in self.books:
            if book.title.lower() == title.lower():
                return book

        return None

    def search_book(self):

        title = input("Enter book title: ")

        book = self.find_book(title)

        if book:
            book.display_details()
        else:
            print("Book not found.")

    def borrow_book(self):

        title = input("Enter book title: ")

        book = self.find_book(title)

        if book:
            book.borrow_book()
        else:
            print("Book not found.")

    def return_book(self):

        title = input("Enter book title: ")

        book = self.find_book(title)

        if book:
            book.return_book()
        else:
            print("Book not found.")
