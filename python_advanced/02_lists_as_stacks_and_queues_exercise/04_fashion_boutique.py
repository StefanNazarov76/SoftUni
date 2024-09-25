from collections import deque

clothes = deque([int(num) for num in input().split()])
rack_capacity = int(input())

racks = 1
current_rack_capacity = rack_capacity

while clothes:
    current_cloth = clothes.popleft()

    if current_cloth > current_rack_capacity:
        racks += 1
        current_rack_capacity = rack_capacity - current_cloth
    else:
        current_rack_capacity -= current_cloth

print(racks)
