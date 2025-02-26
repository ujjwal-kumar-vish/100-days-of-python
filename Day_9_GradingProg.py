student_scores = {
    "Harry" : 81,
    "Ron" : 78,
    "Hermione" : 99,
    "Draco" : 74,
    "Neville" : 62,
}

student_grade = {}

for student in student_scores:
    if student_scores[student] > 90 :
        student_grade[student] = "Outstanding"
    elif student_scores[student] > 80 :
        student_grade[student] = "Exceeds Expectations"
    elif student_scores[student] > 70 :
        student_grade[student] = "Acceptable"
    else:
        student_grade[student] = "Fail"

print(student_grade)