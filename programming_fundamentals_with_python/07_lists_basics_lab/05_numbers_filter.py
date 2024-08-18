n = int(input())

numbers = []
filtered_numbers = []

for _ in range(n):
    current_number = int(input())
    numbers.append(current_number)

command = input()

if command == 'even':
    for number in numbers:
        if number % 2 == 0:
            filtered_numbers.append(number)
elif command == 'odd':
    for number in numbers:
        if number % 2 != 0:
            filtered_numbers.append(number)
elif command == 'negative':
    for number in numbers:
        if number < 0:
            filtered_numbers.append(number)
elif command == 'positive':
    for number in numbers:
        if number >= 0:
            filtered_numbers.append(number)

print(filtered_numbers)
