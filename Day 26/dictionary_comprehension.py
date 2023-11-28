from random import randint

names =["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

students_scores = {name:randint(1, 100) for name in names}
print(students_scores)

# passed_students = {student:students_scores[student] for student in students_scores if students_scores[student] >= 60}

passed_students = {student:score for(student, score) in students_scores.items() if score >= 60}

print(passed_students)