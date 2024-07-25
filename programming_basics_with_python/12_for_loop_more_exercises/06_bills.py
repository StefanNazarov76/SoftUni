months = int(input())

power = 0
water = 0
internet = 0
other = 0

for _ in range(months):
    power_bill = float(input())

    power += power_bill
    water += 20
    internet += 15
    other += (power_bill + 20 + 15) * 1.2

average = (power + water + internet + other) / months

print(f'Electricity: {power:.2f} lv')
print(f'Water: {water:.2f} lv')
print(f'Internet: {internet:.2f} lv')
print(f'Other: {other:.2f} lv')
print(f'Average: {average:.2f} lv')
