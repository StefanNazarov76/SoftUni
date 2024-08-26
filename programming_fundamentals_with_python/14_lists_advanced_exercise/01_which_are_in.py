first_sequence = input().split(', ')
second_sequence = input().split(', ')

substrings = []

for substring in first_sequence:
    for string in second_sequence:
        if substring in string:
            substrings.append(substring)
            break

print(substrings)
