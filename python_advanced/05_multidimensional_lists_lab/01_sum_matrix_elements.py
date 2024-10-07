rows, cols = [int(el) for el in input().split(', ')]

matrix = []

for _ in range(rows):
    data = [int(el) for el in input().split(', ')]
    matrix.append(data)

print(matrix)

