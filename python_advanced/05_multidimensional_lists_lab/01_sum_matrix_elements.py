rows, cols = [int(el) for el in input().split(', ')]

matrix = []

for row in range(rows):
    data = [int(el) for el in input().split(', ')]
    matrix.append(data)

print(matrix)

