fire_cells = input().split('#')
water_amount = int(input())

cells_list = []
total_effort = 0
total_fire = 0

for current_cell in fire_cells:
    fire_type, fire_range = current_cell.split(' = ')
    fire_range = int(fire_range)

    if water_amount < fire_range:
        continue
    elif fire_type == 'High' and 81 <= fire_range <= 125:
        water_amount -= fire_range
        total_fire += fire_range
        total_effort += fire_range * 0.25
        cells_list.append(fire_range)

    elif fire_type == 'Medium' and 51 <= fire_range <= 80:
        water_amount -= fire_range
        total_fire += fire_range
        total_effort += fire_range * 0.25
        cells_list.append(fire_range)

    elif fire_type == 'Low' and 1 <= fire_range <= 50:
        water_amount -= fire_range
        total_fire += fire_range
        total_effort += fire_range * 0.25
        cells_list.append(fire_range)

    if water_amount <= 0:
        break

print('Cells:')
for cell in cells_list:
    print(f' - {cell}')
print(f'Effort: {total_effort:.2f}')
print(f'Total Fire: {total_fire}')
