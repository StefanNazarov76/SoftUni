n = int(input())

students = {}

for _ in range(n):
    name = input()
    grade = float(input())

    if name not in students.keys():
        students[name] = []
    students[name].append(grade)

for name, grades in students.items():
    average_grade = sum(grades) / len(grades)

    if average_grade >= 4.50:
        print(f'{name} -> {average_grade:.2f}')
