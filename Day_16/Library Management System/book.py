class Book:
    """
    Represents a single book in the library.
    """

    def __init__(self):
        self.title = input("Enter book title: ")
        self.author = input("Enter author name: ")
        self.category = input("Enter book category: ")

        self.is_available = True
        self.borrower = ""

    def display_details(self):
        print("\n--------------------")
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Category: {self.category}")

        if self.is_available:
            print("Status: Available")
        else:
            print(f"Status: Borrowed by {self.borrower}")

    def borrow_book(self):
        if self.is_available:
            self.borrower = input("Enter borrower name: ")
            self.is_available = False
            print(f"'{self.title}' borrowed successfully.")
        else:
            print(f"'{self.title}' is already borrowed.")

    def return_book(self):
        if not self.is_available:
            self.is_available = True
            self.borrower = ""
            print(f"'{self.title}' returned successfully.")
        else:
            print(f"'{self.title}' is already available.")

