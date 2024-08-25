wagons = [0] * int(input())
command = input().split()

while command[0] != 'End':
    if 'add' in command:
        people = int(command[1])
        wagons[-1] += people

    elif 'insert' in command:
        index = int(command[1])
        people = int(command[2])

        wagons[index] += people

    elif 'leave' in command:
        index = int(command[1])
        people = int(command[2])

        wagons[index] -= people

    command = input().split()

print(wagons)
