budget = float(input())
category = input()
number_of_people_in_group = int(input())

price_per_ticket = 0
transport_price = 0

if category == "VIP":
    price_per_ticket = 499.99
elif category == "Normal":
    price_per_ticket = 249.99

if number_of_people_in_group <= 4:
    transport_price = budget * 0.75
elif number_of_people_in_group <= 9:
    transport_price = budget * 0.6
elif number_of_people_in_group <= 24:
    transport_price = budget * 0.5
elif number_of_people_in_group <= 49:
    transport_price = budget * 0.4
else:
    transport_price = budget * 0.25

total_price = (number_of_people_in_group * price_per_ticket) + transport_price
diff = abs(budget - total_price)

if budget >= total_price:
    print(f'Yes! You have {diff:.2f} leva left.')
else:
    print(f'Not enough money! You need {diff:.2f} leva.')
