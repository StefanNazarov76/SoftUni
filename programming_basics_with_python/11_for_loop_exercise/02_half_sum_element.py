from sys import maxsize

n = int(input())

max_num = -maxsize
sum = 0

for _ in range(n):
    num = int(input())

    if num > max_num:
        max_num = num

    sum += num

if max_num == (sum - max_num):
    print('Yes')
    print(f'Sum = {max_num}')
else:
    diff = abs(sum - (max_num * 2))
    print('No')
    print(f'Diff = {diff}')
