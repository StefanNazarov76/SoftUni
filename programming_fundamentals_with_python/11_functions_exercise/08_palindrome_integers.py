def is_palindrome(number: str):
    return number == number[::-1]


numbers_as_str = input().split(', ')
for number in numbers_as_str:
    print(is_palindrome(number))
