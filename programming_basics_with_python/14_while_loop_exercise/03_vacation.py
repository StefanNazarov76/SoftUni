vacation_price = float(input())
balance = float(input())

days_counter = 0
spending_days_counter = 0

while balance < vacation_price:
    command = input()
    money = float(input())
    days_counter += 1
    if command == 'spend':
        spending_days_counter += 1
        if money > balance:
            balance = 0
        else:
            balance -= money
        if spending_days_counter == 5:
            print(f"You can't save the money.")
            print(days_counter)
            break
    elif command == 'save':
        balance += money
        spending_days_counter = 0
else:
    print(f'You saved the money for {days_counter} days.')
