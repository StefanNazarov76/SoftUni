command = input()

courses = {}

while command != 'end':
    course, name = command.split(' : ')

    if course not in courses.keys():
        courses[course] = []
    courses[course].append(name)

    command = input()

for course in courses.keys():
    registered_students = len(courses[course])
    print(f'{course}: {registered_students}')

    for name in courses.get(course):
        print(f'-- {name}')
