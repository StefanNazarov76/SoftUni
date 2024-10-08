n = int(input())

primary_diagonal_sum = 0
secondary_diagonal_sum = 0

matrix = [[int(el) for el in input().split()] for _ in range(n)]

for i in range(n):
    primary_diagonal_sum += matrix[i][i]
    secondary_diagonal_sum += matrix[i][n - i - 1]

print(abs(primary_diagonal_sum - secondary_diagonal_sum))
