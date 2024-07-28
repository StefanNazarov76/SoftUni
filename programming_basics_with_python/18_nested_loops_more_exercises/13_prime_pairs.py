number_one = int(input())
number_two = int(input())
number_three = int(input())
number_four = int(input())

for first_number in range(number_one, (number_one + number_three + 1)):
    is_first_number_prime = False
    counter = 0

    for divisor in range(1, first_number + 1):
        if first_number % divisor == 0:
            counter += 1
    if counter == 2:
        is_first_number_prime = True
    else:
        continue

    for second_number in range(number_two, (number_two + number_four + 1)):
        is_second_number_prime = False
        counter = 0

        for divisor in range(1, second_number + 1):
            if second_number % divisor == 0:
                counter += 1
        if counter == 2:
            is_second_number_prime = True
        else:
            continue

        if is_first_number_prime and is_second_number_prime:
            print(f'{first_number}{second_number}')
