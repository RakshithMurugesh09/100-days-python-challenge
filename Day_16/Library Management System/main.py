class Book:
    """
    Represents a single book in the library.
    """

    def __init__(self):
        """
        TODO:
        - Ask the user for:
            * Book Title
            * Author Name
            * Category
        - Store them as instance attributes.
        - Set the book as available by default.
        """
        pass

    def display_details(self):
        """
        TODO:
        Display:
        - Title
        - Author
        - Category
        - Availability Status
        """
        pass

    def borrow_book(self):
        """
        TODO:
        - Check if the book is available.
        - If available:
            * Mark it as borrowed.
            * Display success message.
        - Otherwise:
            * Display that the book is already borrowed.
        """
        pass

    def return_book(self):
        """
        TODO:
        - Check if the book is borrowed.
        - If borrowed:
            * Mark it as available.
            * Display success message.
        - Otherwise:
            * Display that the book is already available.
        """
        pass


def display_logo():
    """
    TODO:
    Display the Library Management System logo.
    """
    pass


def display_menu():
    """
    TODO:
    Display:

    1. Add Book
    2. View All Books
    3. Search Book
    4. Borrow Book
    5. Return Book
    6. Exit

    Return the user's menu choice.
    """
    pass


def add_book(library):
    """
    TODO:
    - Create a Book object.
    - Add it to the library list.
    - Display success message.
    """
    pass


def view_books(library):
    """
    TODO:
    - If no books exist, display a message.
    - Otherwise:
        Loop through the library list.
        Display every book's details.
    """
    pass


def search_book(library):
    """
    TODO:
    - Ask the user for a book title.
    - Search the library list.
    - If found:
        Display the book details.
    - Otherwise:
        Display 'Book not found'.
    """
    pass


def borrow_book(library):
    """
    TODO:
    - Ask the user for a book title.
    - Search for the book.
    - If found:
        Call the book's borrow_book() method.
    - Otherwise:
        Display 'Book not found'.
    """
    pass


def return_book(library):
    """
    TODO:
    - Ask the user for a book title.
    - Search for the book.
    - If found:
        Call the book's return_book() method.
    - Otherwise:
        Display 'Book not found'.
    """
    pass


def main():
    """
    TODO:

    - Display logo.

    - Create an empty library list.

    - Run the program inside a loop.

    - Display menu.

    - Perform the selected operation.

    - Exit when the user chooses Exit.
    """
    pass


if __name__ == "__main__":
    main()