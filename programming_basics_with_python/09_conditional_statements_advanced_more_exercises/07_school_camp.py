season = input()
group_type = input()
students_count = int(input())
nights = int(input())

price = 0
sport = ''

if season == 'Winter':
    if group_type == 'girls':
        price = 9.6
        sport = 'Gymnastics'
    elif group_type == 'boys':
        price = 9.6
        sport = 'Judo'
    elif group_type == 'mixed':
        price = 10
        sport = 'Ski'
elif season == 'Spring':
    if group_type == 'girls':
        price = 7.2
        sport = 'Athletics'
    elif group_type == 'boys':
        price = 7.2
        sport = 'Tennis'
    elif group_type == 'mixed':
        price = 9.5
        sport = 'Cycling'
elif season == 'Summer':
    if group_type == 'girls':
        price = 15
        sport = 'Volleyball'
    elif group_type == 'boys':
        price = 15
        sport = 'Football'
    elif group_type == 'mixed':
        price = 20
        sport = 'Swimming'

total_price = students_count * price * nights

if students_count >= 50:
    total_price *= 0.5
elif students_count >= 20:
    total_price *= 0.85
elif students_count >= 10:
    total_price *= 0.95

print(f'{sport} {total_price:.2f} lv.')
