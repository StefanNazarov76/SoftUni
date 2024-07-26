expected_total_sum = int(input())
command = input()

product_counter = 0
total_sum = 0


payments_with_cash = 0
payments_with_card = 0
total_sum_with_cash = 0
total_sum_with_card = 0

while command != 'End':
    product_price = int(command)
    product_counter += 1

    if product_counter % 2 == 0:
        if product_price < 10:
            print('Error in transaction!')
        else:
            print('Product sold!')
            payments_with_card += 1
            total_sum += product_price
            total_sum_with_card += product_price
    else:
        if product_price > 100:
            print('Error in transaction!')
        else:
            print('Product sold!')
            payments_with_cash += 1
            total_sum += product_price
            total_sum_with_cash += product_price

    if total_sum >= expected_total_sum:
        average_payment_with_cash = total_sum_with_cash / payments_with_cash
        average_payment_with_card = total_sum_with_card / payments_with_card
        print(f'Average CS: {average_payment_with_cash:.2f}')
        print(f'Average CC: {average_payment_with_card:.2f}')
        break

    command = input()
else:
    print('Failed to collect required money for charity.')
