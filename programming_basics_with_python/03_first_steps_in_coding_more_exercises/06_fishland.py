mackerel_price_per_kg = float(input())
sprinkle_price_per_kg = float(input())
bonitos_kgs = float(input())
safrids_kgs = float(input())
mussels_kgs = int(input())

total_bonitos_price = bonitos_kgs * (mackerel_price_per_kg * 1.6)
total_safrids_price = safrids_kgs * (sprinkle_price_per_kg * 1.8)
total_mussels_price = mussels_kgs * 7.5
total_price = total_bonitos_price + total_safrids_price + total_mussels_price

print(f'{total_price:.2f}')
