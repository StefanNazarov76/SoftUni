def perfect_number(number):
    divisors_sum = 0

    for divisor in range(1, number):
        if number % divisor == 0:
            divisors_sum += divisor

    if divisors_sum == number:
        return 'We have a perfect number!'
    else:
        return 'It\'s not so perfect.'


number = int(input())

is_perfect = perfect_number(number)
print(is_perfect)
