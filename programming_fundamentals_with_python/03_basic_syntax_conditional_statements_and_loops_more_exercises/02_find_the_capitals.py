string = input()

indexes = []

for i in range(len(string)):
    if string[i].isupper():
        indexes.append(i)

print(indexes)
