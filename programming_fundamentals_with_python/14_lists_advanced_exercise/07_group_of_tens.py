numbers = [int(number) for number in input().split(', ')]

current_group = 10

while numbers:
    filtered_numbers = [num for num in numbers if num <= current_group]
    print(f'Group of {current_group}\'s: {filtered_numbers}')

    numbers = [num for num in numbers if num not in filtered_numbers]
    current_group += 10
