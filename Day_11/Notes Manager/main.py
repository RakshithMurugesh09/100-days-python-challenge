FILE_NAME = "notes.txt"


def add_note():
    note = input("Enter your note: ")

    with open(FILE_NAME, "a") as file:
        file.write(note + "\n")

    print("✅ Note saved.\n")


def view_notes():
    try:
        with open(FILE_NAME, "r") as file:
            print("\n===== Notes =====")

            for i, note in enumerate(file, start=1):
                print(f"{i}. {note.strip()}")

            print()

    except FileNotFoundError:
        print("❌ No notes found.\n")


def search_notes():
    keyword = input("Enter keyword to search: ").lower()

    try:
        found = False

        with open(FILE_NAME, "r") as file:
            for i, note in enumerate(file, start=1):
                if keyword in note.lower():
                    print(f"{i}. {note.strip()}")
                    found = True

        if not found:
            print("❌ No matching notes found.")

    except FileNotFoundError:
        print("❌ No notes found.")

    print()


def delete_notes():
    confirmation = input(
        "\nDelete all notes? This action cannot be undone. (Y/N): "
    ).lower()

    if confirmation == "y":
        with open(FILE_NAME, "w") as file:
            pass

        print("✅ All notes deleted.\n")
    else:
        print("❌ Operation cancelled.\n")


def menu():
    print("===== Notes Manager =====")

    options = [
        "Add Note",
        "View Notes",
        "Search Notes",
        "Delete All Notes",
        "Exit"
    ]

    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")

    try:
        return int(input("\nEnter your choice: "))
    except ValueError:
        return 0


def main():
    while True:
        choice = menu()

        if choice == 1:
            add_note()

        elif choice == 2:
            view_notes()

        elif choice == 3:
            search_notes()

        elif choice == 4:
            delete_notes()

        elif choice == 5:
            print(" 👋 Exiting program.")
            break

        else:
            print("❌ Invalid choice. Please try again.\n")


if __name__ == "__main__":
    main()