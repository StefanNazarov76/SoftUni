letter = input()

word = ''
hidden_word = ''

c_counter = 0
o_counter = 0
n_counter = 0

last_letter = letter

while letter != 'End':
    if not letter.isalpha():
        letter = input()
        continue

    if letter == 'c':
        c_counter += 1
        if c_counter > 1:
            word += letter
    elif letter == 'o':
        o_counter += 1
        if o_counter > 1:
            word += letter
    elif letter == 'n':
        n_counter += 1
        if n_counter > 1:
            word += letter
    else:
        word += letter

    if c_counter > 0 and o_counter > 0 and n_counter > 0:
        c_counter = 0
        o_counter = 0
        n_counter = 0
        hidden_word += word + ' '
        word = ''

    letter = input()
print(hidden_word)
