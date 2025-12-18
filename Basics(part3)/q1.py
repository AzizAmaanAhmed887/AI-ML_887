info = [
    ("Alice", "Math"),
    ("Bob", "Science"),
    ("Alice", "Science"),
    ("Charlie", "Math"),
    ("Bob", "Science"),
    ("Alice", "English"),
    ("Charlie", "English"),
]

student_courses = {}

for student, course in info:
    if student not in student_courses:
        student_courses[student] = set()  # empty set
    student_courses[student].add(course)  # default initialize unique value

print(student_courses)

for name, courses in info:
    if courses == "English":
        print(f"English: {name}")

courses_set = set()
for name, courses in info:
    courses_set.add(courses)

print(courses_set)
