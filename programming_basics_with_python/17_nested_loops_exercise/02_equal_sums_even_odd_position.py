first_number = int(input())
second_number = int(input())

for current_number in range(first_number, second_number + 1):
    even_sum = 0
    odd_sum = 0
    number_to_string = str(current_number)

    for index, digit in enumerate(number_to_string):
        if index % 2 == 0:
            even_sum += int(digit)
        else:
            odd_sum += int(digit)

    if even_sum == odd_sum:
        print(current_number, end=' ')
