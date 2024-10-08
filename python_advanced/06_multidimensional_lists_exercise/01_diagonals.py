n = int(input())

matrix = [[int(el) for el in input().split(', ')] for _ in range(n)]
primary = [matrix[i][i] for i in range(n)]
secondary = [matrix[i][n - i - 1] for i in range(n)]

print(f'Primary diagonal: {', '.join(str(el) for el in primary)}. Sum: {sum(primary)}')
print(f'Secondary diagonal: {', '.join(str(el) for el in secondary)}. Sum: {sum(secondary)}')
