n = int(input())

points = 0
zero_to_9 = 0
ten_to_19 = 0
twenty_to_29 = 0
thirty_to_39 = 0
forty_to_50 = 0
invalid = 0

for _ in range(n):
    number = int(input())

    if 0 <= number <= 9:
        points += number * 0.2
        zero_to_9 += 1
    elif 10 <= number <= 19:
        points += number * 0.3
        ten_to_19 += 1
    elif 20 <= number <= 29:
        points += number * 0.4
        twenty_to_29 += 1
    elif 30 <= number <= 39:
        points += 50
        thirty_to_39 += 1
    elif 40 <= number <= 50:
        points += 100
        forty_to_50 += 1
    else:
        points /= 2
        invalid += 1

zero_to_9_percentage = (zero_to_9 / n) * 100
ten_to_19_percentage = (ten_to_19 / n) * 100
twenty_to_29_percentage = (twenty_to_29 / n) * 100
thirty_to_39_percentage = (thirty_to_39 / n) * 100
forty_to_50_percentage = (forty_to_50 / n) * 100
invalid_percentage = (invalid / n) * 100

print(f'{points:.2f}')
print(f'From 0 to 9: {zero_to_9_percentage:.2f}%')
print(f'From 10 to 19: {ten_to_19_percentage:.2f}%')
print(f'From 20 to 29: {twenty_to_29_percentage:.2f}%')
print(f'From 30 to 39: {thirty_to_39_percentage:.2f}%')
print(f'From 40 to 50: {forty_to_50_percentage:.2f}%')
print(f'Invalid numbers: {invalid_percentage:.2f}%')
