numbers = input().split()

inverted_numbers = []

for num in numbers:
    num = int(num)
    inverted_numbers.append(-num)

print(inverted_numbers)
