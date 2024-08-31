elements = input().split()

stock = {}

for i in range(0, len(elements), 2):
    food = elements[i]
    quantity = int(elements[i+1])
    stock[food] = quantity

print(stock)
