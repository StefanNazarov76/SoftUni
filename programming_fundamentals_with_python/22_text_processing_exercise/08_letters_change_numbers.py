strings = input().split()

total = 0

for string in strings:
    first_letter = string[0]
    last_letter = string[-1]
    number = int(string[1:-1])

    position = ord(first_letter) - 64
    if first_letter.isupper():
        position = ord(first_letter) - 64
        number /= position
    else:
        position = ord(first_letter) - 96
        number *= position

    if last_letter.isupper():
        position = ord(last_letter) - 64
        number -= position
    else:
        position = ord(last_letter) - 96
        number += position

    total += number

print(f'{total:.2f}')
