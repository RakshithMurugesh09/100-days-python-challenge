from library import Library


def display_menu():

    print("""
1. Add Book
2. View All Books
3. Search Book
4. Borrow Book
5. Return Book
6. Exit
""")

    return input("Enter your choice: ")


def main():

    library = Library()

    while True:

        choice = display_menu()

        if choice == "1":
            library.add_book()

        elif choice == "2":
            library.view_books()

        elif choice == "3":
            library.search_book()

        elif choice == "4":
            library.borrow_book()

        elif choice == "5":
            library.return_book()

        elif choice == "6":
            print("Thank you for using the Library Management System.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()