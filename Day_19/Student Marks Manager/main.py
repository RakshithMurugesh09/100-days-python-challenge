import csv
import os


def add_student():
    student = input("Enter Student Name: ").strip().title()

    if not student:
        print("Student name cannot be empty")
        return

    while True:
        try:
            marks = float(input("Enter Marks: "))

            if marks < 0:
                print("Marks cannot be negative")
                continue

            break

        except ValueError:
            print("Invalid Marks")

    file_exists = os.path.isfile("Student_Marks.csv")

    try:
        with open("Student_Marks.csv", "a", newline="") as csvfile:
            writer = csv.writer(csvfile)

            if not file_exists or os.path.getsize("Student_Marks.csv") == 0:
                writer.writerow(["student", "marks"])

            writer.writerow([student, marks])
            print("\nStudent Marks Added Successfully")

    except IOError as e:
        print(f"Error: {e}")


def view_students():
    try:
        if os.path.getsize("Student_Marks.csv") == 0:
            print("\nNo Student Marks Added")
        else:
            with open("Student_Marks.csv", "r", newline="") as csvfile:
                reader = csv.reader(csvfile)
                next(reader)

                count = 0

                for row in reader:
                    if len(row) < 2:
                        continue

                    print(f"Name: {row[0].title()}, Marks: {row[1]}")
                    count += 1

                print("Total Students: ", count)

    except FileNotFoundError:
        print("Student Marks.csv not found")

    except IOError as e:
        print(f"Error: {e}")


def search_student():
    search = input("Enter Student Name: ").strip().lower()

    try:
        if os.path.getsize("Student_Marks.csv") == 0:
            print("\nNo Student Marks Added")
            return

        with open("Student_Marks.csv", "r", newline="") as csvfile:
            reader = csv.reader(csvfile)
            next(reader, None)

            student = next(
                (row for row in reader if row[0].lower() == search),
                None
            )

            if student:
                print(f"Name: {student[0].title()}, Marks: {student[1]}")
            else:
                print("\nStudent Marks not found")

    except FileNotFoundError:
        print("Student_Marks.csv not found")

    except IOError as e:
        print(f"Error: {e}")


def calculate_average():
    try:
        if os.path.getsize("Student_Marks.csv") == 0:
            print("\nNo Student Marks Added")

        else:
            with open("Student_Marks.csv", "r", newline="") as csvfile:
                reader = csv.reader(csvfile)
                next(reader)

                rows = list(reader)
                total = 0

                for row in rows:
                    total += float(row[1])

                if not rows:
                    print("No student records found.")
                    return

                average = total / len(rows)

                print(
                    f"Total Students: {len(rows)}, "
                    f"Total Average: {average:.2f}"
                )

    except FileNotFoundError:
        print("Student_Marks.csv not found")

    except IOError as e:
        print(f"Error: {e}")


def display_menu():
    print(
        "========== STUDENT MARKS MANAGER =========="
        "\n1. Add Student"
        "\n2. View All Students"
        "\n3. Search Student"
        "\n4. Calculate Average"
        "\n5. Exit"
    )

    try:
        return int(input("\nEnter your choice: "))
    except ValueError:
        return 0


def main():
    while True:
        choice = display_menu()

        if choice == 1:
            add_student()

        elif choice == 2:
            view_students()

        elif choice == 3:
            search_student()

        elif choice == 4:
            calculate_average()

        elif choice == 5:
            print("Thank you for using Student Marks Manager")
            break

        else:
            print("Invalid choice. Please enter 1 to 5.")


main()