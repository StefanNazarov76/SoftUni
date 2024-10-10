line = input().split('|')

sublist = []

for value in line[::-1]:
    sublist.extend(value.split())

print(*sublist)
