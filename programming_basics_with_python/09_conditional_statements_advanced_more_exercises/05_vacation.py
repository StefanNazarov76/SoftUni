budget = float(input())
season = input()

stay_in = ''
location = ''
price = 0

if budget <= 1000:
    stay_in = 'Camp'
    if season == 'Summer':
        location = 'Alaska'
        price = budget * 0.65
    elif season == 'Winter':
        location = 'Morocco'
        price = budget * 0.45
elif budget <= 3000:
    stay_in = 'Hut'
    if season == 'Summer':
        location = 'Alaska'
        price = budget * 0.8
    elif season == 'Winter':
        location = 'Morocco'
        price = budget * 0.6
else:
    stay_in = 'Hotel'
    price = budget * 0.9
    if season == 'Summer':
        location = 'Alaska'
    elif season == 'Winter':
        location = 'Morocco'

print(f'{location} - {stay_in} - {price:.2f}')
