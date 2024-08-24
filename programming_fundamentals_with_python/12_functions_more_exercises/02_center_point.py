from math import floor


def get_center_point(x1, y1, x2, y2):
    if abs(x1) + abs(y1) < abs(x2) + abs(y2):
        return f'({floor(x1)}, {floor(y1)})'
    else:
        return f'({floor(x2)}, {floor(y2)})'


input_x1 = float(input())
input_y1 = float(input())
input_x2 = float(input())
input_y2 = float(input())

center_points = get_center_point(input_x1, input_y1, input_x2, input_y2)
print(center_points)
