chrysanthemums_count = int(input())
roses_count = int(input())
tulips_count = int(input())
season = input()
holiday = input()

total_chrysanthemums_price = 0
total_roses_price = 0
total_tulips_price = 0


if season == "Spring" or season == "Summer":
    total_chrysanthemums_price = chrysanthemums_count * 2
    total_roses_price = roses_count * 4.1
    total_tulips_price = tulips_count * 2.5
elif season == "Autumn" or season == "Winter":
    total_chrysanthemums_price = chrysanthemums_count * 3.75
    total_roses_price = roses_count * 4.5
    total_tulips_price = tulips_count * 4.15

if holiday == "Y":
    total_chrysanthemums_price *= 1.15
    total_roses_price *= 1.15
    total_tulips_price *= 1.15

total_price = total_chrysanthemums_price + total_roses_price + total_tulips_price

if season == "Spring" and tulips_count > 7:
    total_price *= 0.95

if season == "Winter" and roses_count >= 10:
    total_price *= 0.9

if (chrysanthemums_count + roses_count + tulips_count) > 20:
    total_price *= 0.8

print(f'{total_price + 2:.2f}')
