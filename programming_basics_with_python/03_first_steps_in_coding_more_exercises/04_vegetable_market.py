vegetables_price_per_kg = float(input())
fruits_price_per_kg = float(input())
vegetables_kgs = float(input())
fruits_kgs = float(input())

total_vegetables_price = vegetables_kgs * vegetables_price_per_kg
total_fruits_price = fruits_kgs * fruits_price_per_kg
total_price_in_bgn = total_vegetables_price + total_fruits_price
total_price_in_eur = total_price_in_bgn / 1.94

print(f'{total_price_in_eur:.2f}')

