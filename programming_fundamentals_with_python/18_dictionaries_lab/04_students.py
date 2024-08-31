students = []
course_to_search = None

while True:
    data = input()

    if ':' not in data:
        course_to_search = data
        break

    name, id, course = data.split(':')
    students.append({'name': name, 'ID': id, 'Course': course})

for student in students:
    if course_to_search.startswith(student['Course'][0:3]):
        print(f'{student["name"]} - {student["ID"]}')
