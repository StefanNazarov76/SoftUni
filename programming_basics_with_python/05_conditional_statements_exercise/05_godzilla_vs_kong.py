budget = float(input())
statists_count = int(input())
clothes_per_statist_price = float(input())

decor = budget * 0.1
total_clothes_price = statists_count * clothes_per_statist_price

if statists_count > 150:
    total_clothes_price = total_clothes_price * 0.9

amount_needed = decor + total_clothes_price
diff = abs(amount_needed - budget)

if budget >= amount_needed:
    print('Action!')
    print(f'Wingard starts filming with {diff:.2f} leva left.')
else:
    print('Not enough money!')
    print(f'Wingard needs {diff:.2f} leva more.')
