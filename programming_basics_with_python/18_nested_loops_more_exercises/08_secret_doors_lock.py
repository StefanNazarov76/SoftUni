first_number_border = int(input())
second_number_border = int(input())
third_number_border = int(input())


for first_number in range(1, first_number_border + 1):
    if first_number % 2 != 0:
        continue

    for second_number in range(1, second_number_border + 1):
        if second_number < 2:
            continue

        if second_number == 2 or second_number == 3 or second_number == 5 or second_number == 7:
            for third_number in range(1, third_number_border + 1):
                if third_number % 2 != 0:
                    continue

                print(f'{first_number} {second_number} {third_number}')
