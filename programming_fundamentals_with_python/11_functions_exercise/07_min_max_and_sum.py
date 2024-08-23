numbers = input().split()

for i in range(0, len(numbers)):
    numbers[i] = int(numbers[i])

min_number = min(numbers)
max_number = max(numbers)
total_sum = sum(numbers)

print(f'The minimum number is {min_number}')
print(f'The maximum number is {max_number}')
print(f'The sum number is: {total_sum}')
