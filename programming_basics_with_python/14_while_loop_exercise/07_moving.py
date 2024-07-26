width = int(input())
length = int(input())
height = int(input())
boxes = input()

free_space = width * length * height

while boxes != 'Done':
    boxes = int(boxes)

    if free_space > boxes:
        free_space -= boxes
    elif free_space < boxes:
        diff = boxes - free_space
        print(f'No more free space! You need {diff} Cubic meters more.')
        break
    boxes = input()
else:
    print(f'{free_space} Cubic meters left.')
