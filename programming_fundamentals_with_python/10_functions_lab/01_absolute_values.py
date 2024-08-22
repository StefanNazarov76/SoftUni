numbers = input().split()

absolute_values = []

for number in numbers:
    number = float(number)
    absolute_values.append(abs(number))

print(absolute_values)
