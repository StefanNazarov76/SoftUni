secret_message = input().split()
new_message = ''

for element in secret_message:
    element_list = list(element)

    digits = [digit for digit in element_list if digit.isdigit()]
    number = ''.join(digits)
    secret_letter = chr(int(number))

    element_list = [element for element in element_list if not element.isdigit()]
    element_list.insert(0, secret_letter)

    element_list[1], element_list[-1] = element_list[-1], element_list[1]

    new_message += f'{"".join(element_list)} '

print(new_message)
