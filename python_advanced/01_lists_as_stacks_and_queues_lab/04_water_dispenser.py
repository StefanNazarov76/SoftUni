from collections import deque

current_water = int(input())
people = deque()

name = input()
while name != 'Start':
    people.append(name)
    name = input()

command = input()
while command != 'End':
    data = command.split()

    if 'refill' in data:
        _, liters_to_add = data
        current_water += int(liters_to_add)

    else:
        liters_required = int(data[0])
        person = people.popleft()

        if current_water >= liters_required:
            print(f'{person} got water')
            current_water -= liters_required
        else:
            print(f'{person} must wait')

    command = input()

print(f'{current_water} liters left')
