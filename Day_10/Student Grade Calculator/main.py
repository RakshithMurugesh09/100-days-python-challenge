# 📌 Grade Calculator Project - Day 10

def calculate_percentage(marks):
    """
    Calculate the percentage based on marks.
    :param marks: List of marks
    :return: Percentage value
    """
    total = sum(marks)
    percentage = total / len(marks)
    return percentage


def get_grade(percentage):
    """
    Assigns a grade based on the percentage.
    """
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "F"


# ✅ Lambda for pass/fail check
is_pass = lambda percentage: "Pass ✅" if percentage >= 50 else "Fail ❌"


def student_report(name, marks=None):
    """
    Generates a report card for the student.
    If no marks provided, default marks are used.
    """
    if marks is None:
        marks = [75, 80, 65]  # default marks

    percentage = calculate_percentage(marks)
    grade = get_grade(percentage)
    status = is_pass(percentage)

    print("\n📄 STUDENT REPORT")
    print(f"Name       : {name}")
    print(f"Marks      : {marks}")
    print(f"Percentage : {percentage:.2f}%")
    print(f"Grade      : {grade}")
    print(f"Status     : {status}")


# ---------- MAIN PROGRAM ----------
# Taking student details
student_name = input("Enter Student Name: ")

# Enter marks separated by space
marks_input = input("Enter marks for subjects (out of 100), separated by space: ")

if marks_input.strip():  # If marks entered
    marks_list = [int(m) for m in marks_input.split()]
    student_report(student_name, marks_list)
else:
    # Use default marks
    student_report(student_name)
