numbers = input().split()

rounded_numbers = []

for number in numbers:
    number = float(number)
    rounded_numbers.append(round(number))

print(rounded_numbers)
