students_marks = {
    "Alice": 88,
    "Bob": 72,
    "Charlie": 95,
    "Diana": 67,
    "Ethan": 81,
    "Fiona": 90,
    "George": 76,
    "Hannah": 34
}
student_score = {}
for student in students_marks:
    mark = students_marks[student]
    if mark > 90:
        student_score[student] = "First class"
    elif mark> 80:
        student_score[student] = "Second class"
    elif mark > 65:
        student_score[student] = "Pass"
    elif mark < 45:
        student_score[student] = "Fail"
    else:
        student_score[student] = "Just Pass"
print(student_score)
