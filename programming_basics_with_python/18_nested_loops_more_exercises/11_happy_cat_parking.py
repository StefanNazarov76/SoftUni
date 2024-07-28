days = int(input())
hours_per_day = int(input())

total_taxes = 0

for day in range(1, days + 1):
    day_tax = 0

    for hours in range(1, hours_per_day + 1):
        if day % 2 == 0 and hours % 2 != 0:
            total_taxes += 2.50
            day_tax += 2.50
        elif day % 2 != 0 and hours % 2 == 0:
            total_taxes += 1.25
            day_tax += 1.25
        else:
            total_taxes += 1
            day_tax += 1

    print(f'Day: {day} - {day_tax:.2f} leva')

print(f'Total: {total_taxes:.2f} leva')
