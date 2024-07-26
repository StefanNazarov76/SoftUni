bottles_detergent = int(input())
dishes = input()

detergent_left = bottles_detergent * 750
dishwasher_loadings = 0
plates_counter = 0
pots_counter = 0

while dishes != 'End':
    dishes = int(dishes)
    dishwasher_loadings += 1

    if dishwasher_loadings % 3 == 0:
        detergent_left -= dishes * 15
        pots_counter += dishes
    else:
        detergent_left -= dishes * 5
        plates_counter += dishes

    if detergent_left < 0:
        print(f'Not enough detergent, {abs(detergent_left)} ml. more necessary!')
        break

    dishes = input()
else:
    print('Detergent was enough!')
    print(f'{plates_counter} dishes and {pots_counter} pots were washed.')
    print(f'Leftover detergent {detergent_left} ml.')
