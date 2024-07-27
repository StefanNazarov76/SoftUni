destination = input()

while destination != 'End':
    budget = float(input())
    saved_money = 0

    while saved_money < budget:
        current_amount = float(input())
        saved_money += current_amount

        if saved_money >= budget:
            print(f'Going to {destination}!')
            break
    destination = input()
