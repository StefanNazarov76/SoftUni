n = int(input())

for _ in range(n):
    number = int(input())

    if number % 2 == 1:
        print(f'{number} is odd!')
        exit()
else:
    print('All numbers are even.')
