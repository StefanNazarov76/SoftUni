number = int(input())

numbers_sum = 0

while numbers_sum < number:
    current_number = int(input())
    numbers_sum += current_number
else:
    print(numbers_sum)
