text = input()

for index in range(len(text)):
    if text[index] == ':' and index != len(text) - 1:
        emoticon = ':' + text[index + 1]
        print(emoticon)
