string = input()

while string != 'End':
    new_string = ''

    if string == 'SoftUni':
        string = input()
        continue

    for char in string:
        new_string += char * 2

    print(new_string)
    string = input()
