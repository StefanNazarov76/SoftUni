rows = int(input())

matrix = []
diagonal_sum = 0

for _ in range(rows):
    data = [int(el) for el in input().split()]
    matrix.append(data)

for row_index in range(rows):
    diagonal_sum += matrix[row_index][row_index]

print(diagonal_sum)
