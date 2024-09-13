string = input()

unique_symbols_used = 0
message = ''
current_pair = ''

for index in range(len(string)):
    if not string[index].isdigit():
        current_pair += string[index].upper()

    else:
        repetitions = int(string[index])
        message += current_pair * repetitions
        current_pair = ''

print(f'Unique symbols used: {len(set(message))}')
print(message)
