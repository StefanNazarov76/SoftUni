from math import floor, ceil

magnolias_number = int(input())
hyacinths_number = int(input())
roses_number = int(input())
cactuses_number = int(input())
gift_price = float(input())

total_magnolias_price = magnolias_number * 3.25
total_hyacinths_price = hyacinths_number * 4
total_roses_price = roses_number * 3.5
total_cactuses_price = cactuses_number * 8

total_price = total_magnolias_price + total_hyacinths_price + total_roses_price + total_cactuses_price
profit = total_price * 0.95
diff = abs(profit - gift_price)

if profit >= gift_price:
    print(f'She is left with {floor(diff)} leva.')
else:
    print(f'She will have to borrow {ceil(diff)} leva.')
