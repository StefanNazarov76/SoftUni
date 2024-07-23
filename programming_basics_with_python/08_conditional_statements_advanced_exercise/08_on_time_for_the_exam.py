hour_of_exam = int(input())
minutes_of_exam = int(input())
hour_of_arriving = int(input())
minutes_of_arriving = int(input())

exam_time_in_minutes = (hour_of_exam * 60) + minutes_of_exam
arriving_time_in_minutes = (hour_of_arriving * 60) + minutes_of_arriving
diff = abs(exam_time_in_minutes - arriving_time_in_minutes)

if arriving_time_in_minutes > exam_time_in_minutes:
    print('Late')

    if diff >= 60:
        hours = diff // 60
        minutes = diff % 60

        print(f'{hours}:{minutes:02d} hours after the start')
    else:
        print(f'{diff} minutes after the start')
elif arriving_time_in_minutes == exam_time_in_minutes or diff <= 30:
    print('On time')

    if diff > 0:
        print(f'{diff} minutes before the start')
elif arriving_time_in_minutes < exam_time_in_minutes:
    print(f'Early')

    if diff >= 60:
        hours = diff // 60
        minutes = diff % 60

        print(f'{hours}:{minutes:02d} hours before the start')
    else:
        print(f'{diff} minutes before the start')
