offers = input().split(', ')
beggars_count = int(input())

final_offers = []

index = 0

while index < beggars_count:
    current_beggar_final_offer = 0

    for i in range(index, len(offers), beggars_count):
        current_beggar_final_offer += int(offers[i])
    final_offers.append(current_beggar_final_offer)
    index += 1

print(final_offers)
