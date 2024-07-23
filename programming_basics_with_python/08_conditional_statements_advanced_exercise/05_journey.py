budget = float(input())
season = input()

destination = ''
stay_in = ''
price = ''

if budget <= 100:
    destination = 'Bulgaria'
    if season == 'summer':
        stay_in = 'Camp'
        price = budget * 0.3
    elif season == 'winter':
        stay_in = 'Hotel'
        price = budget * 0.7
elif budget <= 1000:
    destination = 'Balkans'
    if season == 'summer':
        stay_in = 'Camp'
        price = budget * 0.4
    elif season == 'winter':
        stay_in = 'Hotel'
        price = budget * 0.8
else:
    destination = 'Europe'
    stay_in = 'Hotel'
    price = budget * 0.9

print(f'Somewhere in {destination}')
print(f'{stay_in} - {price:.2f}')
