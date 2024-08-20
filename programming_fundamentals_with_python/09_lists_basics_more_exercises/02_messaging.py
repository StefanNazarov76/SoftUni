numbers = input().split()
text = input()

message = ''

for number in numbers:
    index = 0
    for digit in number:
        index += int(digit)

    if index >= len(text):
        index -= len(text)

    message += text[index]
    text = text[:index] + text[index+1:]

print(message)
