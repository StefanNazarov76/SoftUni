command = input()

stock = {}

while command != 'statistics':
    product, quantity = command.split(': ')

    if product in stock.keys():
        stock[product] += int(quantity)

    else:
        stock[product] = int(quantity)

    command = input()


products_count = len(stock.keys())
total_quantity = sum(stock.values())

print(f'Products in stock:')
for product in stock.keys():
    print(f'- {product}: {stock[product]}')
print(f'Total Products: {products_count}')
print(f'Total Quantity: {total_quantity}')
