kilometers = int(input())
day_or_night = input()

total_price = 0

if kilometers < 20 and day_or_night == 'day':
    total_price = 0.7 + kilometers * 0.79
elif kilometers < 20 and day_or_night == 'night':
    total_price = 0.7 + kilometers * 0.9
elif kilometers < 100:
    total_price = kilometers * 0.09
else:
    total_price = kilometers * 0.06

print(f'{total_price:.2f}')
