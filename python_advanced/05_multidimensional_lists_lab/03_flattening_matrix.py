rows = int(input())

flattened = []

for _ in range(rows):
    data = [int(el) for el in input().split(', ')]
    flattened.extend(data)

print(flattened)
