from math import floor, ceil

days = int(input())
left_food_in_kgs = int(input())
daily_food_for_dog_in_kgs = float(input())
daily_food_for_cat_in_kgs = float(input())
daily_food_for_turtle_in_grams = float(input())

daily_food_for_turtle_in_kgs = daily_food_for_turtle_in_grams * 0.001

total_dog_food_needed = daily_food_for_dog_in_kgs * days
total_cat_food_needed = daily_food_for_cat_in_kgs * days
total_turtle_food_needed = daily_food_for_turtle_in_kgs * days

total_food_needed = total_dog_food_needed + total_cat_food_needed + total_turtle_food_needed
diff = abs(left_food_in_kgs - total_food_needed)


if left_food_in_kgs >= total_food_needed:
    print(f'{floor(diff)} kilos of food left.')
else:
    print(f'{ceil(diff)} more kilos of food are needed.')
