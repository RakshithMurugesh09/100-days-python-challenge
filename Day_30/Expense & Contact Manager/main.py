import csv
import json
import re

from datetime import datetime


# ============================================
# CONSTANTS
# ============================================

EXPENSE_FILE = "expenses.csv"
CONTACT_FILE = "contacts.json"


# ============================================
# VALIDATION FUNCTIONS
# ============================================

def validate_date(date_string):
    """
    Validate date in DD-MM-YYYY format.

    Return True if valid.
    Return False if invalid.
    """

    # TODO:
    # 1. Check the date format.
    # 2. Use datetime.strptime()
    # 3. Handle invalid dates.
    pass


def validate_phone(phone):
    """
    Validate a 10-digit phone number.

    Return True if valid.
    Return False if invalid.
    """

    # TODO:
    # Use regex to validate phone number.
    pass


def validate_email(email):
    """
    Validate email address.

    Return True if valid.
    Return False if invalid.
    """

    # TODO:
    # Use regex to validate email.
    pass


def get_valid_amount():
    """
    Ask the user for an expense amount.

    Return a valid positive float.
    """

    # TODO:
    # Keep asking until the user enters
    # a valid positive number.
    pass


# ============================================
# EXPENSE FILE FUNCTIONS
# ============================================

def initialize_expense_file():
    """
    Create the expense CSV file with headers
    if it doesn't already exist.
    """

    # TODO:
    # Check whether the CSV file exists.
    # If necessary, create it with:
    #
    # Date, Category, Description, Amount
    pass


def load_expenses():
    """
    Load all expenses from CSV.

    Return a list of expense dictionaries.
    """

    # TODO:
    #
    # Example returned data:
    #
    # [
    #     {
    #         "Date": "24-08-2026",
    #         "Category": "Food",
    #         "Description": "Lunch",
    #         "Amount": "250"
    #     }
    # ]
    pass


def save_expense(expense):
    """
    Save one expense to the CSV file.
    """

    # TODO:
    # Append the expense dictionary
    # to the CSV file.
    pass


# ============================================
# EXPENSE FUNCTIONS
# ============================================

def add_expense():
    """
    Get expense details from the user,
    validate them and save them.
    """

    # TODO:
    #
    # Get:
    # Date
    # Category
    # Description
    # Amount
    #
    # Validate everything.
    #
    # Create an expense dictionary.
    #
    # Save it using save_expense().
    pass


def view_expenses():
    """
    Display all expenses.
    """

    # TODO:
    # Load expenses.
    #
    # If empty, display a message.
    #
    # Otherwise display every expense.
    pass


def search_expenses():
    """
    Search expenses by date, category
    or description.
    """

    # TODO:
    # Ask for a keyword.
    #
    # Search case-insensitively.
    #
    # Display matching expenses.
    pass


def calculate_total():
    """
    Calculate and display total spending.
    """

    # TODO:
    # Load expenses.
    #
    # Convert Amount to float.
    #
    # Calculate total.
    pass


def calculate_average():
    """
    Calculate and display average spending.
    """

    # TODO:
    # Load expenses.
    #
    # Calculate:
    #
    # total / number_of_expenses
    pass


def category_summary():
    """
    Display total spending for each category.
    """

    # TODO:
    #
    # Example:
    #
    # Food       : ₹1500
    # Transport  : ₹2000
    # Shopping   : ₹3500
    #
    # Use a dictionary to store
    # category totals.
    pass


# ============================================
# CONTACT FILE FUNCTIONS
# ============================================

def load_contacts():
    """
    Load contacts from JSON.

    Return a list of contact dictionaries.

    If the JSON file doesn't exist,
    return an empty list.
    """

    # TODO:
    #
    # Handle FileNotFoundError.
    #
    # Handle invalid JSON if necessary.
    pass


def save_contacts(contacts):
    """
    Save all contacts to the JSON file.
    """

    # TODO:
    # Write contacts to JSON.
    #
    # Use indentation so the file
    # is easy for humans to read.
    pass


# ============================================
# CONTACT FUNCTIONS
# ============================================

def add_contact():
    """
    Add a new contact after validation.
    """

    # TODO:
    #
    # Get:
    # Name
    # Phone
    # Email
    #
    # Validate phone and email.
    #
    # Load existing contacts.
    #
    # Check duplicate phone number.
    #
    # Create contact dictionary.
    #
    # Add to list.
    #
    # Save contacts.
    pass


def view_contacts():
    """
    Display all contacts.
    """

    # TODO:
    # Load contacts.
    #
    # If empty, display a message.
    #
    # Otherwise display contacts.
    pass


def search_contact():
    """
    Search for a contact by name,
    phone or email.
    """

    # TODO:
    #
    # Ask for search keyword.
    #
    # Search case-insensitively.
    pass


def update_contact():
    """
    Update an existing contact.
    """

    # TODO:
    #
    # Ask for contact name.
    #
    # Find contact.
    #
    # Ask for new phone/email.
    #
    # Validate new values.
    #
    # Update the contact.
    #
    # Save the updated list.
    pass


def delete_contact():
    """
    Delete an existing contact.
    """

    # TODO:
    #
    # Ask for contact name.
    #
    # Find contact.
    #
    # Ask for confirmation.
    #
    # Delete if confirmed.
    #
    # Save updated contacts.
    pass


# ============================================
# EXPENSE MENU
# ============================================

def expense_menu():
    """
    Display the Expense Manager menu.
    """

    while True:

        print("""
========== EXPENSE MANAGER ==========

1. Add Expense
2. View Expenses
3. Search Expense
4. Total Spending
5. Average Spending
6. Category Summary
7. Back

======================================
""")

        # TODO:
        # Get user's choice.
        # Handle invalid input.

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            search_expenses()

        elif choice == "4":
            calculate_total()

        elif choice == "5":
            calculate_average()

        elif choice == "6":
            category_summary()

        elif choice == "7":
            break

        else:
            print("❌ Invalid choice.")


# ============================================
# CONTACT MENU
# ============================================

def contact_menu():
    """
    Display the Contact Manager menu.
    """

    while True:

        print("""
========== CONTACT MANAGER ==========

1. Add Contact
2. View Contacts
3. Search Contact
4. Update Contact
5. Delete Contact
6. Back

=====================================
""")

        # TODO:
        # Get user's choice.
        # Handle invalid input.

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_contact()

        elif choice == "2":
            view_contacts()

        elif choice == "3":
            search_contact()

        elif choice == "4":
            update_contact()

        elif choice == "5":
            delete_contact()

        elif choice == "6":
            break

        else:
            print("❌ Invalid choice.")


# ============================================
# MAIN MENU
# ============================================

def main():
    """
    Main application menu.
    """

    # TODO:
    # Initialize required files if necessary.

    while True:

        print("""
========================================
       EXPENSE & CONTACT MANAGER
========================================

1. Expense Manager
2. Contact Manager
3. Exit

========================================
""")

        # TODO:
        # Get user choice.
        # Handle invalid input.

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            expense_menu()

        elif choice == "2":
            contact_menu()

        elif choice == "3":
            print("👋 Thank you for using the application.")
            break

        else:
            print("❌ Invalid choice.")


# ============================================
# PROGRAM START
# ============================================

if __name__ == "__main__":
    main()