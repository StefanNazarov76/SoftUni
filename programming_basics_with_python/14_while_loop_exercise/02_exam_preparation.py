poor_grades = int(input())
problem_name = input()

poor_grades_counter = 0
total_grades = 0
problems_counter = 0
last_problem = ''

while problem_name != 'Enough':
    grade = int(input())

    total_grades += grade
    problems_counter += 1
    last_problem = problem_name

    if grade <= 4:
        poor_grades_counter += 1
        if poor_grades_counter == poor_grades:
            print(f'You need a break, {poor_grades_counter} poor grades.')
            break

    problem_name = input()
else:
    average_grade = total_grades / problems_counter
    print(f'Average score: {average_grade:.2f}')
    print(f'Number of problems: {problems_counter}')
    print(f'Last problem: {last_problem}')
