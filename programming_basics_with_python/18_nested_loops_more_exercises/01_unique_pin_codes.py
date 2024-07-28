first_number_limit = int(input())
second_number_limit = int(input())
third_number_limit = int(input())

for pin_one in range(1, first_number_limit + 1):
    if pin_one % 2 == 0:
        for pin_two in range(1, second_number_limit + 1):
            if pin_two == 2 or pin_two == 3 or pin_two == 5 or pin_two == 7:
                for pin_three in range(1, third_number_limit + 1):
                    if pin_three % 2 == 0:
                        print(f'{pin_one} {pin_two} {pin_three}')
