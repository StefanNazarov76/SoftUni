people_data = input()

phonebook = {}

while not people_data.isdigit():
    name, phone_number = people_data.split('-')

    phonebook[name] = phone_number

    people_data = input()

n = int(people_data)

for _ in range(n):
    name = input()

    if name in phonebook:
        print(f'{name} -> {phonebook[name]}')
    else:
        print(f'Contact {name} does not exist.')
