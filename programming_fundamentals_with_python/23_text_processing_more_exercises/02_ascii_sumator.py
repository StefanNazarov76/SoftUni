start = ord(input())
end = ord(input())
string = input()

total = 0

for character in string:
    if start < ord(character) < end:
        total += ord(character)

print(total)
