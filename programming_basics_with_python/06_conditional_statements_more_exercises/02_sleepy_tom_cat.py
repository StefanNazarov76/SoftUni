rest_days = int(input())

work_days = 365 - rest_days
total_playtime_minutes = (work_days * 63) + (rest_days * 127)
free_time = abs(30000 - total_playtime_minutes)

hours = free_time // 60
minutes = free_time % 60

if total_playtime_minutes >= 30000:
    print(f'Tom will run away')
    print(f'{hours} hours and {minutes} minutes more for play')
else:
    print('Tom sleeps well')
    print(f'{hours} hours and {minutes} minutes less for play')
