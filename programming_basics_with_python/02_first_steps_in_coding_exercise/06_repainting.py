sqm_nylon = int(input())
litres_paint = int(input())
litres_thinner = int(input())
hours_for_work = int(input())
bags = 0.4

total_nylon_price = (sqm_nylon + 2) * 1.5
total_paint_price = (litres_paint * 1.1) * 14.5
total_thinner_price = litres_thinner * 5
total_materials_price = total_nylon_price + total_paint_price + total_thinner_price + bags
price_for_work = hours_for_work * (total_materials_price * 0.3)
final_price = total_materials_price + price_for_work

print(final_price)
