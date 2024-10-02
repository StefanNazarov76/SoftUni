n = int(input())

grades_data = {}

for _ in range(n):
    name, grade = input().split()
    grade = float(grade)

    if name not in grades_data:
        grades_data[name] = []

    grades_data[name].append(grade)

for name, grades in grades_data.items():
    average_grade = sum(grades) / len(grades)
    formatted_grades = ' '.join([f'{grade:.2f}' for grade in grades])

    print(f'{name} -> {formatted_grades} (avg: {average_grade:.2f})')
