def mark_attendance():
    """
    Ask the user for:
    - Student name
    - Attendance status (Present/Absent)

    TODO:
    - Validate student name
    - Validate attendance status
    - Append the attendance record to attendance.txt
    - Display a success message
    """
    pass


def view_attendance():
    """
    Display all attendance records.

    TODO:
    - Open attendance.txt in read mode
    - Display each attendance record
    - Handle missing or empty file
    """
    pass


def search_student():
    """
    Search for a student's attendance.

    TODO:
    - Ask for student name
    - Search attendance.txt (case-insensitive)
    - Display the matching record
    - Show 'Student not found' if no match exists
    """
    pass


def count_records():
    """
    Count the total number of attendance records.

    TODO:
    - Read attendance.txt
    - Count valid (non-empty) records
    - Display the total count
    """
    pass


def display_menu():
    """
    Display the Attendance System menu.

    TODO:
    - Print all available options
    - Return the user's choice
    """
    print("========== ATTENDANCE SYSTEM ==========\n"
          "1. Mark Attendance\n"
          "2. View Attendance\n"
          "3. Search Student\n"
          "4. Count Attendance Records\n"
          "5. Exit")

    return input("Enter your choice: ")


def main():
    """
    Main program loop.

    TODO:
    - Display the menu repeatedly
    - Call the appropriate function based on user choice
    - Handle invalid menu choices
    - Exit when the user selects Exit
    """

    while True:
        choice = display_menu()

        if choice == "1":
            mark_attendance()

        elif choice == "2":
            view_attendance()

        elif choice == "3":
            search_student()

        elif choice == "4":
            count_records()

        elif choice == "5":
            print("Thank you for using Attendance System.")
            break

        else:
            print("Invalid choice. Please try again.")


main()