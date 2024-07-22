fuel_type = input()
litres_fuel = float(input())
discount_card = input()

price_per_liter = 0

if fuel_type == "Gas":
    if discount_card == "Yes":
        price_per_liter = 0.85
    else:
        price_per_liter = 0.93
elif fuel_type == "Gasoline":
    if discount_card == "Yes":
        price_per_liter = 2.04
    else:
        price_per_liter = 2.22
elif fuel_type == "Diesel":
    if discount_card == "Yes":
        price_per_liter = 2.21
    else:
        price_per_liter = 2.33

total_price = litres_fuel * price_per_liter

if 20 <= litres_fuel <= 25:
    total_price *= 0.92
elif litres_fuel > 25:
    total_price *= 0.9

print(f"{total_price:.2f} lv.")
