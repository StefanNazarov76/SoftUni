rows, cols = [int(el) for el in input().split()]

matrix = [[el for el in input().split()] for _ in range(rows)]
matches = 0


for row_index in range(rows - 1):
    for col_index in range(cols - 1):
        symbol = matrix[row_index][col_index]

        if (matrix[row_index][col_index + 1] == symbol and matrix[row_index + 1][col_index] == symbol and
                matrix[row_index + 1][col_index + 1] == symbol):
            matches += 1

print(matches)
