age = int(input())
washing_machine_price = float(input())
price_per_toy = int(input())

money = 0
toys = 0
stolen_money = 0

for year in range(1, age + 1):
    if year % 2 == 0:
        money += int(year / 2) * 10
        stolen_money += 1
    else:
        toys += 1

total_money_from_toys = toys * price_per_toy
total_money = total_money_from_toys + money - stolen_money
diff = abs(total_money - washing_machine_price)

if total_money >= washing_machine_price:
    print(f'Yes! {diff:.2f}')
else:
    print(f'No! {diff:.2f}')
