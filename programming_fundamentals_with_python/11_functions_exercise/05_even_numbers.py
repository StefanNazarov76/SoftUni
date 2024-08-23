numbers = input().split()

for i in range(0, len(numbers)):
    numbers[i] = int(numbers[i])

is_even = lambda x: x % 2 == 0
even_numbers = list(filter(is_even, numbers))

print(even_numbers)
