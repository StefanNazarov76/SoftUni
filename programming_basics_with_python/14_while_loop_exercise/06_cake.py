width = int(input())
length = int(input())
pieces = input()

pieces_left = width * length

while pieces != 'STOP':
    pieces = int(pieces)

    if pieces_left > pieces:
        pieces_left -= pieces
    elif pieces_left < pieces:
        diff = pieces - pieces_left
        print(f'No more cake left! You need {diff} pieces more.')
        break
    pieces = input()
else:
    print(f'{pieces_left} pieces are left.')
