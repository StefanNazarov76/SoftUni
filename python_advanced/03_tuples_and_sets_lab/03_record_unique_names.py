n = int(input())

unique_names = set()

for _ in range(n):
    name = input()

    if name not in unique_names:
        unique_names.add(name)

for name in unique_names:
    print(name)
