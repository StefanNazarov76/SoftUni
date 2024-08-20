gifts_list = input().split()
command = input()

while command != 'No Money':
    if 'OutOfStock' in command:
        command, gift = command.split()
        for i in range(len(gifts_list)):
            if gifts_list[i] == gift:
                gifts_list[i] = None

    elif 'Required' in command:
        command, gift, index = command.split()
        index = int(index)
        if 0 <= index < len(gifts_list):
            gifts_list[index] = gift

    elif 'JustInCase' in command:
        command, gift = command.split()
        gifts_list[-1] = gift

    command = input()

for gift in gifts_list:
    if gift:
        print(gift, end=' ')
