elements = input().split()
searched_products = input().split()

stock = {}

for i in range(0, len(elements), 2):
    product = elements[i]
    quantity = int(elements[i+1])
    stock[product] = quantity

for current_product in searched_products:
    if current_product in stock.keys():
        print(f'We have {stock[current_product]} of {current_product} left')
    else:
        print(f'Sorry, we don\'t have {current_product}')
