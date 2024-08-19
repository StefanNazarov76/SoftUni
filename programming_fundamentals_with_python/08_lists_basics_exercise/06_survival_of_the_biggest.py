numbers = input().split()
numbers_to_remove = int(input())

integers = []

for current_number in numbers:
    integers.append(int(current_number))

for _ in range(numbers_to_remove):
    smallest_number = min(integers)
    integers.remove(smallest_number)

print(*integers, sep=', ')
