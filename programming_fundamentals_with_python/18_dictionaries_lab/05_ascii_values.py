characters = input().split(', ')

ascii_values = {}

for character in characters:
    ascii_value = ord(character)
    ascii_values[character] = ascii_value

print(ascii_values)
