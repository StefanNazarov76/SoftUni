rows, cols = [int(el) for el in input().split(', ')]

matrix = []

for row in range(rows):
    data = [int(el) for el in input().split()]
    matrix.append(data)

for col in range(cols):
    sum_col = 0

    for row in range(rows):
        sum_col += matrix[row][col]

    print(sum_col)
