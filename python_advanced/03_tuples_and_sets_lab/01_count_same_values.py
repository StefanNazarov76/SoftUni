numbers = [float(num) for num in input().split()]

occurrences = {}

for num in numbers:
    if num not in occurrences:
        occurrences[num] = numbers.count(num)

for num, occ in occurrences.items():
    print(f'{num} - {occ} times')
