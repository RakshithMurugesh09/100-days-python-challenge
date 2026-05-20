# Day 9 - Contact Book
contact_book = {}

def menu():
    print("\n==== Contact Book ====")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Delete Contact")
    print("4. View All Contacts")
    print("5. Exit")
    try:
        choice = int(input("What is your choice: "))
        return choice
    except ValueError:
        print("Invalid entry. Please enter a number from 1-5.")
        return None

def add_contact():
    print("\n=== Adding Contact ===")
    contact_name = input("Enter name: ").title().strip()

    if contact_name in contact_book:
        need_to_replace = input(f"Contact '{contact_name}' already exists. Replace details? (Y/N): ").upper().strip()
        if need_to_replace != 'Y':
            print(f"No changes made for {contact_name}.")
            return

    try:
        contact_number = int(input("Enter phone number: ").strip())
        contact_book[contact_name] = contact_number
        print("✅ Contact added successfully!")
    except ValueError:
        print("❌ Invalid phone number. Please enter digits only.")

def search_contact():
    search_name = input("Enter name to search: ").title().strip()
    if search_name in contact_book:
        print(f"📞 {search_name}: {contact_book[search_name]}")
    else:
        print("❌ Contact not found.")

def delete_contact():
    contact_name = input("Enter name to delete: ").title().strip()
    if contact_name in contact_book:
        contact_book.pop(contact_name)
        print("🗑️ Contact deleted successfully!")
    else:
        print("❌ Contact not found.")

def view_all_contacts():
    if not contact_book:
        print("📭 No contacts found.")
    else:
        print("\n=== All Contacts ===")
        for name, number in contact_book.items():
            print(f"{name}: {number}")

while True:
    decision = menu()
    if decision == 1:
        add_contact()
    elif decision == 2:
        search_contact()
    elif decision == 3:
        delete_contact()
    elif decision == 4:
        view_all_contacts()
    elif decision == 5:
        print("👋 Exiting Contact Book... Goodbye!")
        break
    elif decision is None:
        continue
    else:
        print("❌ Invalid choice. Please select between 1-5.")
