trip = float(input())
puzzle_count = int(input())
dolls_count = int(input())
teddy_count = int(input())
minions_count = int(input())
trucks_count = int(input())

price_for_all_toys = (puzzle_count * 2.6) + (dolls_count * 3) + (teddy_count * 4.1) + (minions_count * 8.2) + (trucks_count * 2)
all_toys_count = puzzle_count + dolls_count + teddy_count + minions_count + trucks_count

if all_toys_count >= 50:
    price_for_all_toys *= 0.75

total_income = price_for_all_toys * 0.9

if total_income >= trip:
    print(f'Yes! {total_income - trip:.2f} lv left.')
else:
    print(f'Not enough money! {abs(total_income - trip):.2f} lv needed.')
