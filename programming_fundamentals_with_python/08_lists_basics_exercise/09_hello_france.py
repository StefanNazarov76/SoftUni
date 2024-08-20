items = input().split('|')
budget = float(input())

prices = []
profit = 0

for item in items:
    item_type, item_price = item.split('->')
    item_price = float(item_price)

    if budget < item_price:
        continue

    elif item_type == 'Clothes' and item_price <= 50:
        budget -= item_price
        prices.append(item_price)

    elif item_type == 'Shoes' and item_price <= 35:
        budget -= item_price
        prices.append(item_price)

    elif item_type == 'Accessories' and item_price <= 20.50:
        budget -= item_price
        prices.append(item_price)

for price in prices:
    updated_price = price * 1.4
    budget += updated_price
    profit += updated_price - price
    print(f'{updated_price:.2f}', end=' ')
print()
print(f'Profit: {profit:.2f}')

if budget >= 150:
    print('Hello, France!')
else:
    print('Not enough money.')
