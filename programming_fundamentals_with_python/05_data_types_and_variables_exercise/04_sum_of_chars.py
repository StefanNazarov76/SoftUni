n = int(input())

total = 0

for letter in range(n):
    current_letter = ord(input())
    total += current_letter

print(f'The sum equals: {total}')
