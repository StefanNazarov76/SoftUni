numbers_list = input().split(', ')

for i in range(0, len(numbers_list)):
    numbers_list[i] = int(numbers_list[i])

for number in numbers_list:
    if number == 0:
        numbers_list.remove(number)
        numbers_list.append(number)

print(numbers_list)
