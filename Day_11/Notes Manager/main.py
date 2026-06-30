# File name where notes will be stored
FILE_NAME = "notes.txt"


def add_note():
    """Add a new note to the file."""

    # Get note input from the user
    note = input("Enter your note: ").strip()

    # Prevent empty notes from being saved
    if not note:
        print("❌ Note cannot be empty.\n")
        return

    # Append the note to the file
    with open(FILE_NAME, "a") as file:
        file.write(note + "\n")

    print("✅ Note saved.\n")


def view_notes():
    """Display all saved notes."""

    try:
        # Read all notes from the file
        with open(FILE_NAME, "r") as file:
            notes = file.readlines()

            # Check if the file contains any notes
            if not notes:
                print("\n❌ No notes available.\n")
                return

            print("\n===== Notes =====")

            # Display notes with numbering
            for i, note in enumerate(notes, start=1):
                print(f"{i}. {note.strip()}")

            print()

    except FileNotFoundError:
        # Handle case where file does not exist
        print("❌ No notes found.\n")


def search_notes():
    """Search for notes containing a keyword."""

    # Get search keyword from user
    keyword = input("Enter keyword to search: ").strip().lower()

    try:
        found = False

        # Read all notes from the file
        with open(FILE_NAME, "r") as file:
            notes = file.readlines()

            print("\n===== Matching Notes =====")

            # Search each note for the keyword
            for i, note in enumerate(notes, start=1):
                if keyword in note.lower():
                    print(f"{i}. {note.strip()}")
                    found = True

            # Show message if no matching notes are found
            if not found:
                print("❌ No matching notes found.")

    except FileNotFoundError:
        print("❌ No notes found.")

    print()


def delete_notes():
    """Delete all notes after user confirmation."""

    # Ask user for confirmation before deleting notes
    confirmation = input(
        "\nDelete all notes? This action cannot be undone. (Y/N): "
    ).strip().lower()

    if confirmation == "y":
        # Open file in write mode to clear its contents
        with open(FILE_NAME, "w"):
            pass

        print("✅ All notes deleted.\n")
    else:
        print("❌ Operation cancelled.\n")


def menu():
    """Display the menu and return the user's choice."""

    print("===== Notes Manager =====")

    options = [
        "Add Note",
        "View Notes",
        "Search Notes",
        "Delete All Notes",
        "Exit"
    ]

    # Display menu options
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")

    try:
        # Return user's menu selection
        return int(input("\nEnter your choice: "))
    except ValueError:
        # Return 0 for invalid input
        return 0


def main():
    """Main program loop."""

    while True:
        choice = menu()

        # Execute action based on user's choice
        if choice == 1:
            add_note()

        elif choice == 2:
            view_notes()

        elif choice == 3:
            search_notes()

        elif choice == 4:
            delete_notes()

        elif choice == 5:
            print("👋 Exiting program.")
            break

        else:
            print("❌ Invalid choice. Please try again.\n")


# Run the program only if this file is executed directly
if __name__ == "__main__":
    main()