hours = int(input())
minutes = int(input())

total_time_in_minutes = (hours * 60) + minutes + 15

new_hours = total_time_in_minutes // 60
new_minutes = total_time_in_minutes % 60

if new_hours > 23:
    new_hours = 0

print(f'{new_hours}:{new_minutes:02}')
