letters = input()

new_string = ''
previous_letter = None

for letter in letters:
    if letter != previous_letter:
        previous_letter = letter
        new_string += letter

print(new_string)
