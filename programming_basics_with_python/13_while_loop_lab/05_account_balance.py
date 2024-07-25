installment = input()

total_sum = 0

while installment != "NoMoreMoney":
    installment = float(installment)

    if installment < 0:
        print('Invalid operation!')
        print(f'Total: {total_sum:.2f}')
        break
    else:
        total_sum += installment
        print(f'Increase: {installment:.2f}')
    installment = input()
else:
    print(f'Total: {total_sum:.2f}')
