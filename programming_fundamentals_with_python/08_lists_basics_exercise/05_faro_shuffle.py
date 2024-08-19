deck = input().split()
shuffles = int(input())

for _ in range(shuffles):
    middle = len(deck) // 2
    left_part = deck[0:middle]
    right_part = deck[middle:]

    shuffled_deck = []

    for i in range(len(left_part)):
        shuffled_deck.append(left_part[i])
        shuffled_deck.append(right_part[i])
    deck = shuffled_deck

print(deck)
