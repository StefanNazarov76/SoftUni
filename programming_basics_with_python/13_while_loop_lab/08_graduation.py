name = input()
poor_grades = 0
years = 0
total_grades = 0

while True:
    current_grade = float(input())

    if current_grade < 4:
        poor_grades += 1
        if poor_grades > 1:
            print(f'{name} has been excluded at {years + 1} grade')
            break
    else:
        years += 1
        total_grades += current_grade

    if years == 12:
        average_grade = total_grades / years
        print(f'{name} graduated. Average grade: {average_grade:.2f}')
        break
