command = input()

products = {}

while command != 'buy':
    name, price, quantity = command.split()
    price = float(price)
    quantity = int(quantity)

    if name not in products:
        products[name] = [price, quantity]
    else:
        products[name][0] = price
        products[name][1] += quantity

    command = input()

for product in products:
    total_price = products[product][0] * products[product][1]

    print(f'{product} -> {total_price:.2f}')
