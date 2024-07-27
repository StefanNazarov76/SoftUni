start = int(input())
end = int(input())
magical_number = int(input())

combinations_counter = 0

for first_number in range(start, end+1):
    for second_number in range(start, end+1):
        combinations_counter += 1
        if first_number + second_number == magical_number:
            print(f'Combination N:{combinations_counter} ({first_number} + {second_number} = {magical_number})')
            exit()
else:
    print(f'{combinations_counter} combinations - neither equals {magical_number}')
