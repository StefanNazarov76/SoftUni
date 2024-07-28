total_coins_per_one = int(input())
total_coins_per_two = int(input())
total_banknotes_per_five = int(input())
total_sum = int(input())

for coin_per_one in range(0, total_coins_per_one + 1):
    coins_per_one_count = coin_per_one * 1

    for coin_per_two in range(0, total_coins_per_two + 1):
        coins_per_two_count = coin_per_two * 2

        for banknote_per_five in range(0, total_banknotes_per_five + 1):
            banknotes_per_five_count = banknote_per_five * 5

            if coins_per_one_count + coins_per_two_count + banknotes_per_five_count == total_sum:
                print(f'{coin_per_one} * 1 lv. + {coin_per_two} * 2 lv. + {banknote_per_five} * 5 lv. = {total_sum} lv.')
