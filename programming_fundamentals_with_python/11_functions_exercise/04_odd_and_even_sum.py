def get_odd_and_even_sum(number: str):
    odd_sum = 0
    even_sum = 0

    for digit in number:
        digit = int(digit)

        if digit % 2 == 0:
            even_sum += digit
        else:
            odd_sum += digit

    return f'Odd sum = {odd_sum}, Even sum = {even_sum}'


number = input()

result = get_odd_and_even_sum(number)
print(result)
