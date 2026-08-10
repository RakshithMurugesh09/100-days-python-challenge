from functools import reduce

students = [
    {"name": "Rakshith", "marks": 85},
    {"name": "Anu", "marks": 42}
]


def display_menu():
    print("\n========== STUDENT GRADING SYSTEM ==========")
    print("1. Add Student")
    print("2. View Students")
    print("3. Display Grades")
    print("4. Show Passed Students")
    print("5. Statistics")
    print("6. Exit")

    try:
        return int(input("Enter your choice: "))
    except ValueError:
        print("Please enter a valid number.")
        return 0


def calculate_grade(marks):
    return (
        "A" if 90 <= marks <= 100 else
        "B" if 75 <= marks <= 89 else
        "C" if 60 <= marks <= 74 else
        "D" if 35 <= marks <= 59 else
        "F"
    )


def get_valid_marks():
    while True:
        try:
            marks = int(input("Enter Marks: "))
            if 0 <= marks <= 100:
                return marks

            print("Marks must be between 0 and 100.")

        except ValueError:
            print("Please enter a valid number.")


def add_student():
    while True:
        name = input("Enter Student Name: ").strip().title()

        if name:
            break

        print("Name cannot be empty.")

    marks = get_valid_marks()
    students.append({"name": name,"marks": marks})

    print("Student added successfully!")


def view_students():
    if not students:
        print("No students found.")
        return

    print("\n========== STUDENTS ==========")

    for student in students:
        print(f"Name  : {student['name']}")
        print(f"Marks : {student['marks']}")
        print("--------------------------")


def display_grades():
    if not students:
        print("No students found.")
        return

    grades = map(
        lambda s: f"{s['name']} : {s['marks']} : {calculate_grade(s['marks'])}",
        students
    )

    print("\n========== GRADES ==========")

    for grade in grades:
        print(grade)


def show_passed_students():
    if not students:
        print("No students found.")
        return

    passed_students = filter(
        lambda s: s["marks"] >= 35,
        students
    )

    print("\n========== PASSED STUDENTS ==========")

    found = False

    for student in passed_students:
        found = True
        print(
            f"{student['name']} : "
            f"{student['marks']} : "
            f"{calculate_grade(student['marks'])}"
        )

    if not found:
        print("No students passed.")


def display_statistics():
    if not students:
        print("No students found.")
        return

    marks = list(
        map(
            lambda s: s["marks"],
            students
        )
    )

    print("\n========== STATISTICS ==========")
    print("Total Students :", len(students))
    print("Highest Marks  :", max(marks))
    print("Lowest Marks   :", min(marks))
    print("Total Marks    :", reduce(lambda x, y: x + y, marks))
    print("Average Marks  :", round(sum(marks) / len(marks), 2))


def main():
    while True:

        choice = display_menu()

        match choice:

            case 1:
                add_student()

            case 2:
                view_students()

            case 3:
                display_grades()

            case 4:
                show_passed_students()

            case 5:
                display_statistics()

            case 6:
                print("Exiting...")
                break

main()