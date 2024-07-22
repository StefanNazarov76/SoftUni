from math import floor, ceil

sqm_vineyards = int(input())
grape_per_sqm = float(input())
liters_wine_needed = int(input())
workers_number = int(input())

total_grapes = sqm_vineyards * grape_per_sqm
total_wine = (total_grapes * 0.4) / 2.5
wine_left = total_wine - liters_wine_needed
wine_for_workers = wine_left / workers_number

if total_wine >= liters_wine_needed:
    print(f"Good harvest this year! Total wine: {floor(total_wine)} liters.\n{ceil(wine_left)} liters left -> "
          f"{ceil(wine_for_workers)} liters per person.")
else:
    diff = liters_wine_needed - total_wine
    print(f"It will be a tough winter! More {floor(diff)} liters wine needed.")
