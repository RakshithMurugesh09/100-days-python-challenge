import csv
import json
import os
import re

from datetime import datetime


# ============================================
# CONSTANTS
# ============================================

EXPENSE_FILE = "expenses.csv"
CONTACT_FILE = "contacts.json"

EXPENSE_HEADERS = ["Date", "Category", "Description", "Amount"]


# ============================================
# VALIDATION FUNCTIONS
# ============================================

def validate_date(date_string):
    """
    Validate a date in DD-MM-YYYY format.

    Args:
        date_string (str): Date entered by the user.

    Returns:
        bool: True if valid, otherwise False.
    """

    try:
        datetime.strptime(date_string, "%d-%m-%Y")
        return True
    except ValueError:
        return False


def validate_phone(phone):
    """
    Validate a 10-digit Indian phone number.

    Args:
        phone (str): Phone number entered by the user.

    Returns:
        bool: True if valid, otherwise False.
    """

    # Allows exactly 10 digits.
    phone_pattern = r"^\d{10}$"

    return bool(re.fullmatch(phone_pattern, phone))


def validate_email(email):
    """
    Validate an email address.

    Args:
        email (str): Email address entered by the user.

    Returns:
        bool: True if valid, otherwise False.
    """

    email_pattern = (
        r"^[A-Za-z0-9._%+-]+"
        r"@[A-Za-z0-9.-]+"
        r"\.[A-Za-z]{2,}$"
    )

    return bool(re.fullmatch(email_pattern, email))


def get_valid_amount():
    """
    Ask the user for an expense amount.

    Returns:
        float: A valid positive expense amount.
    """

    while True:
        amount_input = input("Enter expense amount: ₹").strip()

        # Allow a user to enter commas, for example: 1,500.50
        amount_input = amount_input.replace(",", "")

        try:
            amount = float(amount_input)

            if amount <= 0:
                print("❌ Amount must be greater than zero.")
                continue

            return round(amount, 2)

        except ValueError:
            print("❌ Invalid amount. Enter a valid positive number.")


def get_non_empty_input(prompt):
    """
    Keep asking until the user enters a non-empty value.

    Args:
        prompt (str): Message displayed to the user.

    Returns:
        str: A non-empty user input.
    """

    while True:
        value = input(prompt).strip()

        if value:
            return value

        print("❌ This field cannot be empty.")


def pause():
    """
    Pause the program until the user presses Enter.
    """

    input("\nPress Enter to continue...")


# ============================================
# DISPLAY FUNCTIONS
# ============================================

def display_expense(expense, number=None):
    """
    Display one expense in a readable format.

    Args:
        expense (dict): Expense dictionary.
        number (int | None): Optional expense number.
    """

    heading = f"Expense {number}" if number is not None else "Expense"

    try:
        amount = float(expense.get("Amount", 0))
    except (ValueError, TypeError):
        amount = 0.0

    print("-" * 45)
    print(heading)
    print("-" * 45)
    print(f"Date        : {expense.get('Date', '')}")
    print(f"Category    : {expense.get('Category', '')}")
    print(f"Description : {expense.get('Description', '')}")
    print(f"Amount      : ₹{amount:,.2f}")


def display_contact(contact, number=None):
    """
    Display one contact in a readable format.

    Args:
        contact (dict): Contact dictionary.
        number (int | None): Optional contact number.
    """

    heading = f"Contact {number}" if number is not None else "Contact"

    print("-" * 45)
    print(heading)
    print("-" * 45)
    print(f"Name  : {contact.get('Name', '')}")
    print(f"Phone : {contact.get('Phone', '')}")
    print(f"Email : {contact.get('Email', '')}")


# ============================================
# EXPENSE FILE FUNCTIONS
# ============================================

def initialize_expense_file():
    """
    Create the expense CSV file with headers
    if it does not exist or is empty.
    """

    try:
        file_does_not_exist = not os.path.exists(EXPENSE_FILE)
        file_is_empty = (
            os.path.exists(EXPENSE_FILE)
            and os.path.getsize(EXPENSE_FILE) == 0
        )

        if file_does_not_exist or file_is_empty:
            with open(
                EXPENSE_FILE,
                mode="w",
                newline="",
                encoding="utf-8"
            ) as file:
                writer = csv.DictWriter(
                    file,
                    fieldnames=EXPENSE_HEADERS
                )
                writer.writeheader()

    except OSError as error:
        print(f"❌ Unable to initialize expense file: {error}")


def load_expenses():
    """
    Load all expenses from the CSV file.

    Returns:
        list: A list of expense dictionaries.
    """

    initialize_expense_file()

    try:
        with open(
            EXPENSE_FILE,
            mode="r",
            newline="",
            encoding="utf-8"
        ) as file:
            reader = csv.DictReader(file)

            if reader.fieldnames is None:
                return []

            return list(reader)

    except FileNotFoundError:
        return []

    except (OSError, csv.Error) as error:
        print(f"❌ Unable to load expenses: {error}")
        return []


def save_expense(expense):
    """
    Append one expense dictionary to the CSV file.

    Args:
        expense (dict): Expense information.

    Returns:
        bool: True if saved successfully, otherwise False.
    """

    initialize_expense_file()

    try:
        with open(
            EXPENSE_FILE,
            mode="a",
            newline="",
            encoding="utf-8"
        ) as file:
            writer = csv.DictWriter(
                file,
                fieldnames=EXPENSE_HEADERS
            )
            writer.writerow(expense)

        return True

    except (OSError, csv.Error) as error:
        print(f"❌ Unable to save expense: {error}")
        return False


# ============================================
# EXPENSE FUNCTIONS
# ============================================

def add_expense():
    """
    Get expense details from the user,
    validate them and save them.
    """

    print("\n========== ADD EXPENSE ==========\n")

    while True:
        date = input(
            "Enter date in DD-MM-YYYY format "
            "or press Enter for today's date: "
        ).strip()

        if not date:
            date = datetime.now().strftime("%d-%m-%Y")

        if validate_date(date):
            break

        print("❌ Invalid date. Use DD-MM-YYYY format.")

    category = get_non_empty_input("Enter category: ").title()
    description = get_non_empty_input("Enter description: ")
    amount = get_valid_amount()

    expense = {
        "Date": date,
        "Category": category,
        "Description": description,
        "Amount": f"{amount:.2f}"
    }

    if save_expense(expense):
        print("\n✅ Expense added successfully.")
        display_expense(expense)

    pause()


def view_expenses():
    """
    Display all expenses.
    """

    print("\n========== ALL EXPENSES ==========\n")

    expenses = load_expenses()

    if not expenses:
        print("ℹ️ No expenses found.")
        pause()
        return

    for number, expense in enumerate(expenses, start=1):
        display_expense(expense, number)

    print("-" * 45)
    print(f"Total records: {len(expenses)}")

    pause()


def search_expenses():
    """
    Search expenses by date, category,
    description or amount.
    """

    print("\n========== SEARCH EXPENSE ==========\n")

    expenses = load_expenses()

    if not expenses:
        print("ℹ️ No expenses available to search.")
        pause()
        return

    keyword = get_non_empty_input(
        "Enter date, category, description or amount: "
    ).casefold()

    matching_expenses = []

    for expense in expenses:
        searchable_values = [
            expense.get("Date", ""),
            expense.get("Category", ""),
            expense.get("Description", ""),
            expense.get("Amount", "")
        ]

        if any(
            keyword in str(value).casefold()
            for value in searchable_values
        ):
            matching_expenses.append(expense)

    if not matching_expenses:
        print(f"\n❌ No expense found matching '{keyword}'.")
        pause()
        return

    print(f"\n✅ Found {len(matching_expenses)} matching expense(s).\n")

    for number, expense in enumerate(matching_expenses, start=1):
        display_expense(expense, number)

    pause()


def calculate_total():
    """
    Calculate and display total spending.
    """

    print("\n========== TOTAL SPENDING ==========\n")

    expenses = load_expenses()

    if not expenses:
        print("ℹ️ No expenses found.")
        pause()
        return

    total = 0.0
    skipped_records = 0

    for expense in expenses:
        try:
            total += float(expense.get("Amount", 0))
        except (ValueError, TypeError):
            skipped_records += 1

    print(f"Total number of expenses : {len(expenses)}")
    print(f"Total spending           : ₹{total:,.2f}")

    if skipped_records:
        print(
            f"⚠️ Invalid amount records skipped: "
            f"{skipped_records}"
        )

    pause()


def calculate_average():
    """
    Calculate and display average spending.
    """

    print("\n========== AVERAGE SPENDING ==========\n")

    expenses = load_expenses()

    if not expenses:
        print("ℹ️ No expenses found.")
        pause()
        return

    valid_amounts = []

    for expense in expenses:
        try:
            valid_amounts.append(
                float(expense.get("Amount", 0))
            )
        except (ValueError, TypeError):
            continue

    if not valid_amounts:
        print("❌ No valid expense amounts are available.")
        pause()
        return

    total = sum(valid_amounts)
    average = total / len(valid_amounts)

    print(f"Number of valid expenses : {len(valid_amounts)}")
    print(f"Total spending           : ₹{total:,.2f}")
    print(f"Average spending         : ₹{average:,.2f}")

    pause()


def category_summary():
    """
    Display total spending for each category.
    """

    print("\n========== CATEGORY SUMMARY ==========\n")

    expenses = load_expenses()

    if not expenses:
        print("ℹ️ No expenses found.")
        pause()
        return

    category_totals = {}

    for expense in expenses:
        category = expense.get("Category", "Uncategorized").strip()

        if not category:
            category = "Uncategorized"

        try:
            amount = float(expense.get("Amount", 0))
        except (ValueError, TypeError):
            continue

        normalized_category = category.title()

        category_totals[normalized_category] = (
            category_totals.get(normalized_category, 0) + amount
        )

    if not category_totals:
        print("❌ No valid expense data is available.")
        pause()
        return

    sorted_categories = sorted(
        category_totals.items(),
        key=lambda item: item[1],
        reverse=True
    )

    print(f"{'Category':<25}{'Total':>18}")
    print("-" * 43)

    for category, total in sorted_categories:
        print(f"{category:<25}₹{total:>17,.2f}")

    print("-" * 43)
    print(
        f"{'Overall Total':<25}"
        f"₹{sum(category_totals.values()):>17,.2f}"
    )

    pause()


# ============================================
# CONTACT FILE FUNCTIONS
# ============================================

def initialize_contact_file():
    """
    Create the contacts JSON file if it does not exist.
    """

    if os.path.exists(CONTACT_FILE):
        return

    try:
        with open(
            CONTACT_FILE,
            mode="w",
            encoding="utf-8"
        ) as file:
            json.dump([], file, indent=4)

    except OSError as error:
        print(f"❌ Unable to initialize contact file: {error}")


def load_contacts():
    """
    Load contacts from the JSON file.

    Returns:
        list: A list of contact dictionaries.
    """

    initialize_contact_file()

    try:
        with open(
            CONTACT_FILE,
            mode="r",
            encoding="utf-8"
        ) as file:
            content = file.read().strip()

            if not content:
                return []

            contacts = json.loads(content)

            if not isinstance(contacts, list):
                print(
                    "❌ Invalid contact file structure. "
                    "Expected a list."
                )
                return []

            return contacts

    except FileNotFoundError:
        return []

    except json.JSONDecodeError:
        print(
            "❌ contacts.json contains invalid JSON. "
            "Please correct or delete the file."
        )
        return []

    except OSError as error:
        print(f"❌ Unable to load contacts: {error}")
        return []


def save_contacts(contacts):
    """
    Save all contacts to the JSON file.

    Args:
        contacts (list): List of contact dictionaries.

    Returns:
        bool: True if saved successfully, otherwise False.
    """

    try:
        with open(
            CONTACT_FILE,
            mode="w",
            encoding="utf-8"
        ) as file:
            json.dump(
                contacts,
                file,
                indent=4,
                ensure_ascii=False
            )

        return True

    except (OSError, TypeError) as error:
        print(f"❌ Unable to save contacts: {error}")
        return False


# ============================================
# CONTACT HELPER FUNCTIONS
# ============================================

def phone_exists(contacts, phone, ignored_index=None):
    """
    Check whether a phone number already exists.

    Args:
        contacts (list): Existing contacts.
        phone (str): Phone number to verify.
        ignored_index (int | None): Contact index to ignore.

    Returns:
        bool: True if the phone number exists.
    """

    for index, contact in enumerate(contacts):
        if ignored_index is not None and index == ignored_index:
            continue

        if contact.get("Phone", "") == phone:
            return True

    return False


def email_exists(contacts, email, ignored_index=None):
    """
    Check whether an email address already exists.

    Args:
        contacts (list): Existing contacts.
        email (str): Email address to verify.
        ignored_index (int | None): Contact index to ignore.

    Returns:
        bool: True if the email already exists.
    """

    for index, contact in enumerate(contacts):
        if ignored_index is not None and index == ignored_index:
            continue

        existing_email = contact.get("Email", "")

        if existing_email.casefold() == email.casefold():
            return True

    return False


def find_contacts_by_name(contacts, name):
    """
    Find contacts whose names contain the search value.

    Args:
        contacts (list): Existing contacts.
        name (str): Name to search.

    Returns:
        list: List containing matching indexes and contacts.
    """

    matches = []

    for index, contact in enumerate(contacts):
        contact_name = contact.get("Name", "")

        if name.casefold() in contact_name.casefold():
            matches.append((index, contact))

    return matches


def select_contact(contacts, action):
    """
    Ask the user to select a contact by name.

    Args:
        contacts (list): Existing contacts.
        action (str): Action description.

    Returns:
        int | None: Selected contact index or None.
    """

    search_name = get_non_empty_input(
        f"Enter the contact name to {action}: "
    )

    matches = find_contacts_by_name(contacts, search_name)

    if not matches:
        print(f"❌ No contact found matching '{search_name}'.")
        return None

    if len(matches) == 1:
        return matches[0][0]

    print("\nMultiple contacts were found:\n")

    for option_number, (_, contact) in enumerate(
        matches,
        start=1
    ):
        print(
            f"{option_number}. "
            f"{contact.get('Name', '')} | "
            f"{contact.get('Phone', '')} | "
            f"{contact.get('Email', '')}"
        )

    while True:
        selection = input(
            "\nSelect contact number or enter 0 to cancel: "
        ).strip()

        if not selection.isdigit():
            print("❌ Enter a valid number.")
            continue

        selection_number = int(selection)

        if selection_number == 0:
            return None

        if 1 <= selection_number <= len(matches):
            selected_index = matches[selection_number - 1][0]
            return selected_index

        print("❌ Invalid contact selection.")


# ============================================
# CONTACT FUNCTIONS
# ============================================

def add_contact():
    """
    Add a new contact after validation.
    """

    print("\n========== ADD CONTACT ==========\n")

    name = get_non_empty_input("Enter name: ").title()
    contacts = load_contacts()

    while True:
        phone = input("Enter 10-digit phone number: ").strip()

        # Remove commonly entered separators.
        phone = phone.replace(" ", "").replace("-", "")

        if not validate_phone(phone):
            print("❌ Phone number must contain exactly 10 digits.")
            continue

        if phone_exists(contacts, phone):
            print("❌ A contact with this phone number already exists.")
            continue

        break

    while True:
        email = input("Enter email address: ").strip().lower()

        if not validate_email(email):
            print("❌ Enter a valid email address.")
            continue

        if email_exists(contacts, email):
            print("❌ A contact with this email address already exists.")
            continue

        break

    contact = {
        "Name": name,
        "Phone": phone,
        "Email": email
    }

    contacts.append(contact)

    if save_contacts(contacts):
        print("\n✅ Contact added successfully.")
        display_contact(contact)

    pause()


def view_contacts():
    """
    Display all contacts.
    """

    print("\n========== ALL CONTACTS ==========\n")

    contacts = load_contacts()

    if not contacts:
        print("ℹ️ No contacts found.")
        pause()
        return

    sorted_contacts = sorted(
        contacts,
        key=lambda contact: contact.get(
            "Name",
            ""
        ).casefold()
    )

    for number, contact in enumerate(sorted_contacts, start=1):
        display_contact(contact, number)

    print("-" * 45)
    print(f"Total contacts: {len(contacts)}")

    pause()


def search_contact():
    """
    Search for a contact by name, phone or email.
    """

    print("\n========== SEARCH CONTACT ==========\n")

    contacts = load_contacts()

    if not contacts:
        print("ℹ️ No contacts available to search.")
        pause()
        return

    keyword = get_non_empty_input(
        "Enter name, phone or email: "
    ).casefold()

    matching_contacts = []

    for contact in contacts:
        searchable_values = [
            contact.get("Name", ""),
            contact.get("Phone", ""),
            contact.get("Email", "")
        ]

        if any(
            keyword in str(value).casefold()
            for value in searchable_values
        ):
            matching_contacts.append(contact)

    if not matching_contacts:
        print(f"\n❌ No contact found matching '{keyword}'.")
        pause()
        return

    print(f"\n✅ Found {len(matching_contacts)} contact(s).\n")

    for number, contact in enumerate(
        matching_contacts,
        start=1
    ):
        display_contact(contact, number)

    pause()


def update_contact():
    """
    Update an existing contact.

    Pressing Enter keeps the existing value.
    """

    print("\n========== UPDATE CONTACT ==========\n")

    contacts = load_contacts()

    if not contacts:
        print("ℹ️ No contacts available to update.")
        pause()
        return

    contact_index = select_contact(contacts, "update")

    if contact_index is None:
        print("ℹ️ Update cancelled.")
        pause()
        return

    contact = contacts[contact_index]

    print("\nCurrent contact information:")
    display_contact(contact)

    print(
        "\nEnter new information. "
        "Press Enter to keep the current value."
    )

    while True:
        new_name = input(
            f"Name [{contact.get('Name', '')}]: "
        ).strip()

        if not new_name:
            new_name = contact.get("Name", "")

        if new_name:
            new_name = new_name.title()
            break

        print("❌ Name cannot be empty.")

    while True:
        new_phone = input(
            f"Phone [{contact.get('Phone', '')}]: "
        ).strip()

        if not new_phone:
            new_phone = contact.get("Phone", "")
            break

        new_phone = new_phone.replace(" ", "").replace("-", "")

        if not validate_phone(new_phone):
            print("❌ Phone number must contain exactly 10 digits.")
            continue

        if phone_exists(
            contacts,
            new_phone,
            ignored_index=contact_index
        ):
            print("❌ Another contact already uses this phone number.")
            continue

        break

    while True:
        new_email = input(
            f"Email [{contact.get('Email', '')}]: "
        ).strip()

        if not new_email:
            new_email = contact.get("Email", "")
            break

        new_email = new_email.lower()

        if not validate_email(new_email):
            print("❌ Enter a valid email address.")
            continue

        if email_exists(
            contacts,
            new_email,
            ignored_index=contact_index
        ):
            print("❌ Another contact already uses this email address.")
            continue

        break

    updated_contact = {
        "Name": new_name,
        "Phone": new_phone,
        "Email": new_email
    }

    contacts[contact_index] = updated_contact

    if save_contacts(contacts):
        print("\n✅ Contact updated successfully.")
        display_contact(updated_contact)

    pause()


def delete_contact():
    """
    Delete an existing contact after confirmation.
    """

    print("\n========== DELETE CONTACT ==========\n")

    contacts = load_contacts()

    if not contacts:
        print("ℹ️ No contacts available to delete.")
        pause()
        return

    contact_index = select_contact(contacts, "delete")

    if contact_index is None:
        print("ℹ️ Deletion cancelled.")
        pause()
        return

    contact = contacts[contact_index]

    print("\nContact selected for deletion:")
    display_contact(contact)

    while True:
        confirmation = input(
            "\nAre you sure you want to delete this contact? "
            "(yes/no): "
        ).strip().casefold()

        if confirmation in {"yes", "y"}:
            deleted_contact = contacts.pop(contact_index)

            if save_contacts(contacts):
                print(
                    f"\n✅ Contact "
                    f"'{deleted_contact.get('Name', '')}' "
                    f"deleted successfully."
                )

            break

        if confirmation in {"no", "n"}:
            print("\nℹ️ Deletion cancelled.")
            break

        print("❌ Enter yes or no.")

    pause()


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
            print("Returning to the main menu...")
            break

        else:
            print("❌ Invalid choice. Enter a number from 1 to 7.")


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
            print("Returning to the main menu...")
            break

        else:
            print("❌ Invalid choice. Enter a number from 1 to 6.")


# ============================================
# MAIN MENU
# ============================================

def main():
    """
    Initialize required files and display
    the main application menu.
    """

    initialize_expense_file()
    initialize_contact_file()

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

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            expense_menu()

        elif choice == "2":
            contact_menu()

        elif choice == "3":
            print("\n👋 Thank you for using the application.")
            break

        else:
            print("❌ Invalid choice. Enter a number from 1 to 3.")


# ============================================
# PROGRAM START
# ============================================

if __name__ == "__main__":
    main()