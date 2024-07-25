from sys import maxsize

number = input()

min_number = maxsize

while number != 'Stop':
    number = int(number)
    if number < min_number:
        min_number = number
    number = input()
else:
    print(min_number)
