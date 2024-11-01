def print_rhombus_upper_part(size):
    for row in range(1, size + 1):
        print(f'{" " * (size - row)}{"* " * row}')


def print_rhombus_bottom_part(size):
    for row in range(size - 1, 0, -1):
        print(f'{" " * (size - row)}{"* " * row}')


def print_rhombus(size):
    print_rhombus_upper_part(size)
    print_rhombus_bottom_part(size)


n = int(input())
print_rhombus(n)
