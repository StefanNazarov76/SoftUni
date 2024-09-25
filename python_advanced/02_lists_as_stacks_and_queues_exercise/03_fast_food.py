from collections import deque

food_quantity = int(input())
orders = deque([int(num) for num in input().split()])

print(max(orders))

while orders:
    current_order = orders.popleft()

    if food_quantity >= current_order:
        food_quantity -= current_order
    else:
        print(f"Orders left: ", current_order, *orders)
        break
else:
    print('Orders complete')
