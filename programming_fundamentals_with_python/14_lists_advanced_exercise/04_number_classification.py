def positive_numbers(list_of_numbers):
    return ', '.join([str(number) for number in list_of_numbers if number >= 0])


def negative_numbers(list_of_numbers):
    return ', '.join([str(number) for number in list_of_numbers if number < 0])


def even_numbers(list_of_numbers):
    return ', '.join([str(number) for number in list_of_numbers if number % 2 == 0])


def odd_numbers(list_of_numbers):
    return ', '.join([str(number) for number in list_of_numbers if number % 2 != 0])


numbers = [int(number) for number in input().split(', ')]

print(f'Positive: {positive_numbers(numbers)}')
print(f'Negative: {negative_numbers(numbers)}')
print(f'Even: {even_numbers(numbers)}')
print(f'Odd: {odd_numbers(numbers)}')
