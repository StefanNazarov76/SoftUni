def triangle_upper_part(size):
    for row in range(1, size + 1):
        for number in range(1, row + 1):
            print(number, end=' ')
        print()


def triangle_lower_part(size):
    for row in range(size - 1, 0, -1):
        for number in range(1, row + 1):
            print(number, end=' ')
        print()


def print_triangle(size):
    triangle_upper_part(size)
    triangle_lower_part(size)
