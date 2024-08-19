factor = int(input())
n = int(input())

numbers = []

for i in range(1, n + 1):
    numbers.append(factor * i)

print(numbers)
