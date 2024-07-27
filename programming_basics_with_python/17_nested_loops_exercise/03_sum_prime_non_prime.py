command = input()

prime_numbers_sum = 0
non_prime_numbers_sum = 0

while command != 'stop':
    number = int(command)

    if number < 0:
        print(f'Number is negative.')
        command = input()
        continue

    counter = 0
    for divisor in range(1, number + 1):
        if number % divisor == 0:
            counter += 1

    if counter == 2:
        prime_numbers_sum += number
    else:
        non_prime_numbers_sum += number

    command = input()

print(f'Sum of all prime numbers is: {prime_numbers_sum}')
print(f'Sum of all non prime numbers is: {non_prime_numbers_sum}')
