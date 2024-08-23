numbers = input().split()

for i in range(0, len(numbers)):
    numbers[i] = int(numbers[i])

sorted_numbers = sorted(numbers)

print(sorted_numbers)
