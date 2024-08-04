n = int(input())

for first_number in range(n):
    for second_number in range(n):
        for third_number in range(n):
            print(f'{chr(97 + first_number)}{chr(97 + second_number)}{chr(97 + third_number)}')
