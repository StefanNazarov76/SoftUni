start_letter = ord(input())
end_letter = ord(input())
avoid_letter = ord(input())

combinations = 0

for first_letter in range(start_letter, end_letter + 1):
    for second_letter in range(start_letter, end_letter + 1):
        for third_letter in range(start_letter, end_letter + 1):
            if first_letter == avoid_letter or second_letter == avoid_letter or third_letter == avoid_letter:
                continue

            print(f'{chr(first_letter)}{chr(second_letter)}{chr(third_letter)}', end=' ')
            combinations += 1

print(combinations)
