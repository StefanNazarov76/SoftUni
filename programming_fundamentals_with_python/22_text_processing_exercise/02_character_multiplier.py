first_string, second_string = input().split()

total = 0

for index1, index2 in zip(first_string, second_string):
    total += ord(index1) * ord(index2)

if len(first_string) > len(second_string):
    for index in range(len(second_string), len(first_string)):
        total += ord(first_string[index])

if len(first_string) < len(second_string):
    for index in range(len(first_string), len(second_string)):
        total += ord(second_string[index])

print(total)
