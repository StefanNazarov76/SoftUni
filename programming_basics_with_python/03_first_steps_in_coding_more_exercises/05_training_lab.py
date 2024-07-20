w = float(input())
h = float(input())

rows = w // 1.2
desks_per_row = (h - 1) // 0.7
total_desks = (rows * desks_per_row) - 3

print(f'{total_desks:.0f}')
