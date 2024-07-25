students_count = int(input())

total_grade = 0
two_to_three = 0
three_to_four = 0
four_to_five = 0
five_or_more = 0

for _ in range(students_count):
    current_grade = float(input())
    total_grade += current_grade

    if current_grade < 3:
        two_to_three += 1
    elif current_grade < 4:
        three_to_four += 1
    elif current_grade < 5:
        four_to_five += 1
    else:
        five_or_more += 1

average_grade = total_grade / students_count
two_to_three_percentage = (two_to_three / students_count) * 100
three_to_four_percentage = (three_to_four / students_count) * 100
four_to_five_percentage = (four_to_five / students_count) * 100
five_or_more_percentage = (five_or_more / students_count) * 100

print(f'Top students: {five_or_more_percentage:.2f}%')
print(f'Between 4.00 and 4.99: {four_to_five_percentage:.2f}%')
print(f'Between 3.00 and 3.99: {three_to_four_percentage:.2f}%')
print(f'Fail: {two_to_three_percentage:.2f}%')
print(f'Average: {average_grade:.2f}')
