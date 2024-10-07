import sys

rows, cols = [int(el) for el in input().split(', ')]

matrix = []
sub_matrix = []
max_sum = -sys.maxsize

for _ in range(rows):
    data = [int(el) for el in input().split(', ')]
    matrix.append(data)

for row_index in range(rows - 1):
    for col_index in range(cols - 1):
        current_element = matrix[row_index][col_index]
        next_element = matrix[row_index][col_index + 1]
        below_element = matrix[row_index + 1][col_index]
        diagonal_element = matrix[row_index + 1][col_index + 1]

        current_sum = current_element + next_element + below_element + diagonal_element

        if current_sum > max_sum:
            max_sum = current_sum
            sub_matrix = [[current_element, next_element], [below_element, diagonal_element]]


print(*sub_matrix[0])
print(*sub_matrix[1])
print(max_sum)
