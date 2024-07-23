junior_bikers_number = int(input())
senior_bikers_number = int(input())
road = input()

total_junior_price = 0
total_senior_price = 0

if road == 'trail':
    total_junior_price = junior_bikers_number * 5.5
    total_senior_price = senior_bikers_number * 7
elif road == 'cross-country':
    total_junior_price = junior_bikers_number * 8
    total_senior_price = senior_bikers_number * 9.5
    if (junior_bikers_number + senior_bikers_number) >= 50:
        total_junior_price *= 0.75
        total_senior_price *= 0.75
elif road == 'downhill':
    total_junior_price = junior_bikers_number * 12.25
    total_senior_price = senior_bikers_number * 13.75
elif road == 'road':
    total_junior_price = junior_bikers_number * 20
    total_senior_price = senior_bikers_number * 21.5

total_price = (total_junior_price + total_senior_price) * 0.95

print(f'{total_price:.2f}')
