jury_count = int(input())
presentation_name = input()

grades_sum = 0
grades_count = 0

while presentation_name != 'Finish':
    presentation_grades_sum = 0

    for _ in range(jury_count):
        grade = float(input())
        grades_sum += grade
        grades_count += 1
        presentation_grades_sum += grade

    average_presentation_grade = presentation_grades_sum / jury_count
    print(f'{presentation_name} - {average_presentation_grade:.2f}.')

    presentation_name = input()
else:
    final_grade = grades_sum / grades_count
    print(f"Student's final assessment is {final_grade:.2f}.")
