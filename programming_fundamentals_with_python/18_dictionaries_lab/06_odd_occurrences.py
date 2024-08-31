words = input().split()

dictionary = {}

for word in words:
    word = word.lower()

    if word not in dictionary:
        dictionary[word] = 0

    dictionary[word] += 1

for word in dictionary:
    if dictionary[word] % 2 != 0:
        print(word, end=' ')
