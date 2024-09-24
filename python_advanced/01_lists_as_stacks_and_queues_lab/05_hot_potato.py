from collections import deque

names = deque(input().split())
n = int(input()) - 1

while len(names) > 1:
    names.rotate(-n)
    removed_kid = names.popleft()

    print(f'Removed {removed_kid}')

print(f'Last is {names.popleft()}')
