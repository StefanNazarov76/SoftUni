n = int(input())

current_number = 0

for row in range(1, n + 1):
    for col in range(1, row + 1):
        current_number += 1

        if current_number > n:
            exit()
        else:
            print(current_number, end=' ')
    print()
