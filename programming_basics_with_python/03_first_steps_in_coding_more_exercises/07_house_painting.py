x = float(input())
y = float(input())
h = float(input())

door = 1.2 * 2
window = 1.5 * 1.5

front_wall = x * x - door
back_wall = x * x
side_wall = x * y - window
paint_for_walls = (front_wall + back_wall + 2 * side_wall) / 3.4

main_roof = x * y
side_roof = (x * h) / 2
paint_for_roof = ((main_roof + side_roof) * 2) / 4.3

print(f"{paint_for_walls:.2f}")
print(f"{paint_for_roof:.2f}")