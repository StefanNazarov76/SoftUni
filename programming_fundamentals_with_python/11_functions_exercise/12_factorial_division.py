def calculate_factorial(number):
    factorial = 1
    for current_number in range(1, number + 1):
        factorial *= current_number

    return factorial


first_number = int(input())
second_number = int(input())

first_factorial = calculate_factorial(first_number)
second_factorial = calculate_factorial(second_number)
result = first_factorial / second_factorial

print(f'{result:.2f}')
