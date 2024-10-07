n = int(input())

matrix = []

for _ in range(n):
    data = [el for el in input()]
    matrix.append(data)

symbol = input()

for row_index in range(n):
    for col_index in range(n):
        if matrix[row_index][col_index] == symbol:
            print(f'({row_index}, {col_index})')
            exit()

print(f'{symbol} does not occur in the matrix')
