def get_characters_in_range(start, end):
    characters = []

    for char in range(ord(start) + 1, ord(end)):
        characters.append(chr(char))

    return ' '.join(characters)


first_character = input()
second_character = input()

result = get_characters_in_range(first_character, second_character)
print(result)
