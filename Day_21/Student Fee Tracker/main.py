FILE_NAME = "Fee_Details.txt"


def add_payment():
    """Add a student fee payment."""

    while True:
        student_name = input("Enter Student Name: ").strip().title()

        if student_name:
            break

        print("❌ Student name cannot be empty.")

    while True:
        try:
            fee_amount = float(input("Enter Fee Amount: ₹"))

            if fee_amount > 0:
                break

            print("❌ Amount must be greater than 0.")

        except ValueError:
            print("❌ Please enter a valid amount.")

    with open(FILE_NAME, "a") as file:
        file.write(f"{student_name} - {fee_amount}\n")

    print("✅ Payment recorded successfully.")


def view_payments():
    """Display all payment records."""

    try:
        with open(FILE_NAME, "r") as file:
            records = file.readlines()

            if not records:
                print("📭 No payment records found.")
                return

            print("\n===== PAYMENT RECORDS =====")

            for record in records:
                print(record.strip())

    except FileNotFoundError:
        print("❌ No payment file found.")


def search_student():
    """Search for a student payment record."""

    while True:
        student_name = input("Enter Student Name: ").strip()

        if student_name:
            break

        print("❌ Student name cannot be empty.")

    try:
        found = False

        with open(FILE_NAME, "r") as file:
            for line in file:

                if student_name.lower() in line.lower():
                    print("\n✅ Record Found")
                    print(line.strip())
                    found = True
                    break

        if not found:
            print("❌ Student not found.")

    except FileNotFoundError:
        print("❌ No payment file found.")


def total_collection():
    """Calculate total fee collection."""

    try:
        total = 0

        with open(FILE_NAME, "r") as file:
            for line in file:

                if line.strip():
                    name, amount = line.strip().split(" - ")
                    total += float(amount)

        print(f"💰 Total Collection: ₹{total:.2f}")

    except FileNotFoundError:
        print("❌ No payment file found.")


def display_menu():
    """Display menu."""

    print("\n========== STUDENT FEE TRACKER ==========")
    print("1. Add Fee Payment")
    print("2. View Payments")
    print("3. Search Student")
    print("4. Total Collection")
    print("5. Exit")

    return input("Enter your choice: ").strip()


def main():
    """Main program."""

    while True:

        choice = display_menu()

        if choice == "1":
            add_payment()

        elif choice == "2":
            view_payments()

        elif choice == "3":
            search_student()

        elif choice == "4":
            total_collection()

        elif choice == "5":
            print("👋 Thank you for using Student Fee Tracker.")
            break

        else:
            print("❌ Invalid choice. Please try again.")


main()