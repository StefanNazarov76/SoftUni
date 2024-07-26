change = float(input())

change_remaining = int(change * 100)
coins_counter = 0

while change_remaining > 0:
    if change_remaining >= 200:
        coins_counter += 1
        change_remaining -= 200
    elif change_remaining >= 100:
        coins_counter += 1
        change_remaining -= 100
    elif change_remaining >= 50:
        coins_counter += 1
        change_remaining -= 50
    elif change_remaining >= 20:
        coins_counter += 1
        change_remaining -= 20
    elif change_remaining >= 10:
        coins_counter += 1
        change_remaining -= 10
    elif change_remaining >= 5:
        coins_counter += 1
        change_remaining -= 5
    elif change_remaining >= 2:
        coins_counter += 1
        change_remaining -= 2
    elif change_remaining >= 1:
        coins_counter += 1
        change_remaining -= 1
else:
    print(coins_counter)
