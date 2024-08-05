key = int(input())
lines = int(input())

word = ''

for _ in range(lines):
    current_letter = input()
    word += chr(key + ord(current_letter))

print(word)
