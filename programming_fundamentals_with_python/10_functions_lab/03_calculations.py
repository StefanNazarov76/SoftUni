def calculate_result(operator, num1, num2):
    result = None

    if operator == 'multiply':
        result = num1 * num2
    elif operator == 'divide':
        result = int(num1 / num2)
    elif operator == 'add':
        result = num1 + num2
    elif operator == 'subtract':
        result = num1 - num2

    return result


operator = input()
first_number = int(input())
second_number = int(input())

result = calculate_result(operator, first_number, second_number)
print(result)
