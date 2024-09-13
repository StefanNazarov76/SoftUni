string = input()

new_string = ''
explosion = 0

for index in range(len(string)):
    if explosion == 0 and string[index] != '>':
        new_string += string[index]

    elif string[index] == '>':
        explosion += int(string[index + 1])
        new_string += string[index]

    else:
        explosion -= 1

print(new_string)
