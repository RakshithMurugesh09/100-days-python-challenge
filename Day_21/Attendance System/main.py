FILE_NAME = "Attendance.txt"


def mark_attendance():
    """Add a student's attendance record."""

    while True:
        student_name = input("Enter Student Name: ").strip().title()
        if student_name:
            break
        print("❌ Student name cannot be empty.")

    while True:
        attendance_status = input("Enter Attendance (P/A): ").strip().upper()
        if attendance_status in ["P", "A"]:
            break

        print("❌ Please enter only P or A.")

    with open(FILE_NAME, "a") as attendance_file:
        attendance_file.write(f"{student_name} - {attendance_status}\n")

    print("✅ Attendance saved successfully.")


def view_attendance():
    """Display all attendance records."""

    try:
        with open(FILE_NAME, "r") as attendance_file:
            records = attendance_file.readlines()

            if not records:
                print("📭 No attendance records found.")
                return

            print("\n===== ATTENDANCE RECORDS =====")

            for record in records:
                print(record.strip())

    except FileNotFoundError:
        print("❌ Attendance file not found.")


def search_student():
    """Search a student record."""

    while True:
        student_name = input("Enter Student Name: ").strip()

        if student_name:
            break

        print("❌ Student name cannot be empty.")

    try:
        found = False

        with open(FILE_NAME, "r") as attendance_file:
            for line in attendance_file:

                if student_name.lower() in line.lower():
                    print("\n✅ Record Found")
                    print(line.strip())
                    found = True
                    break

        if not found:
            print("❌ Student not found.")

    except FileNotFoundError:
        print("❌ Attendance file not found.")


def count_records():
    """Count attendance records."""

    try:
        with open(FILE_NAME, "r") as attendance_file:
            record_count = sum(1 for line in attendance_file if line.strip())

        print(f"📊 Total Attendance Records: {record_count}")

    except FileNotFoundError:
        print("❌ Attendance file not found.")


def display_menu():
    """Display menu."""

    print("\n========== ATTENDANCE SYSTEM ==========")
    print("1. Mark Attendance")
    print("2. View Attendance")
    print("3. Search Student")
    print("4. Count Attendance Records")
    print("5. Exit")

    return input("Enter your choice: ").strip()


def main():
    """Main program."""

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
            print("👋 Thank you for using Attendance System.")
            break

        else:
            print("❌ Invalid choice. Please try again.")


main()