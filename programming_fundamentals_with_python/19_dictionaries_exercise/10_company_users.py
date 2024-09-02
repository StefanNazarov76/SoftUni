command = input()

companies = {}

while command != 'End':
    company, employee = command.split(' -> ')

    if company not in companies.keys():
        companies[company] = []

    if employee not in companies.get(company):
        companies[company].append(employee)

    command = input()

for company in companies.keys():
    print(f'{company}')

    for employee in companies.get(company):
        print(f'-- {employee}')
