chicken_menus_count = int(input())
fish_menus_count = int(input())
vegetarian_menus_count = int(input())

total_chicken_menus_price = chicken_menus_count * 10.35
total_fish_menus_price = fish_menus_count * 12.4
total_vegetarian_menus_price = vegetarian_menus_count * 8.15
total_menus_price = total_chicken_menus_price + total_fish_menus_price + total_vegetarian_menus_price
desert_price = total_menus_price * 0.2
final_price = total_menus_price + desert_price + 2.5

print(final_price)
