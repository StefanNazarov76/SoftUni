size = int(input())
matrix = [[int(el) for el in input().split()] for _ in range(size)]

command = input()
while command != 'END':
    command_type, row, col, value = command.split()
    row, col, value = int(row), int(col), int(value)

    if not (0 <= row < size and 0 <= col < size):
        print('Invalid coordinates')
        command = input()
        continue

    if command_type == 'Add':
        matrix[row][col] += value

    elif command_type == 'Subtract':
        matrix[row][col] -= value

    command = input()

[print(*row) for row in matrix]
