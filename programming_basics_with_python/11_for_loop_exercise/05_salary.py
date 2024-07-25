opened_tabs = int(input())
salary = int(input())

for _ in range(opened_tabs):
    current_tab = input()

    if current_tab == 'Facebook':
        salary -= 150
    elif current_tab == 'Instagram':
        salary -= 100
    elif current_tab == 'Reddit':
        salary -= 50

    if salary <= 0:
        print('You have lost your salary.')
        break
else:
    print(f'{salary:.0f}')
