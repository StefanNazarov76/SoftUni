groups_count = int(input())

musala = 0
monblan = 0
kilimanjaro = 0
k2 = 0
everest = 0

for _ in range(groups_count):
    current_group = int(input())

    if current_group <= 5:
        musala += current_group
    elif current_group <= 12:
        monblan += current_group
    elif current_group <= 25:
        kilimanjaro += current_group
    elif current_group <= 40:
        k2 += current_group
    else:
        everest += current_group

total_people = musala + monblan + kilimanjaro + k2 + everest
musala_percentage = (musala / total_people) * 100
monblan_percentage = (monblan / total_people) * 100
kilimanjaro_percentage = (kilimanjaro / total_people) * 100
k2_percentage = (k2 / total_people) * 100
everest_percentage = (everest / total_people) * 100

print(f'{musala_percentage:.2f}%')
print(f'{monblan_percentage:.2f}%')
print(f'{kilimanjaro_percentage:.2f}%')
print(f'{k2_percentage:.2f}%')
print(f'{everest_percentage:.2f}%')
