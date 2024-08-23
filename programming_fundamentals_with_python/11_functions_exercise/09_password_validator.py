
def password_validator(password):
    is_valid = True

    if 6 > len(password) or len(password) > 10:
        is_valid = False
        print('Password must be between 6 and 10 characters')

    if not password.isalnum():
        is_valid = False
        print('Password must consist only of letters and digits')

    digit_counter = 0
    for char in password:
        if char.isdigit():
            digit_counter += 1
    if digit_counter < 2:
        is_valid = False
        print('Password must have at least 2 digits')

    if is_valid:
        print('Password is valid')


password = input()
password_validator(password)
