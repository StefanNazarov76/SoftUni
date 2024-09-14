n = int(input())

for person in range(n):
    current_person = input()

    name_start, name_end = current_person.index('@'), current_person.index('|')
    age_start, age_end = current_person.index('#'), current_person.index('*')

    print(f'{current_person[name_start + 1:name_end]} is {current_person[age_start + 1:age_end]} years old.')
    