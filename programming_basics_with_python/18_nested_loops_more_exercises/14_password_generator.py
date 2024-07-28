n = int(input())
l = int(input())

start_symbol_three = ord('a')

for first_symbol in range(1, n):
    for second_symbol in range(1, n + 2):
        for third_symbol in range(start_symbol_three, start_symbol_three + l):
            for fourth_symbol in range(start_symbol_three, start_symbol_three + l):
                for fifth_symbol in range(1, n + 3):

                    if first_symbol < fifth_symbol <= n and fifth_symbol > second_symbol:
                        print(f"{first_symbol}{second_symbol}{chr(third_symbol)}{chr(fourth_symbol)}{fifth_symbol}",
                              end=" ")
