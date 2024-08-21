numbers_list = input().split()
k = int(input())

result_list = []
counter = 0
index = 0

for i in range(0, len(numbers_list)):
    numbers_list[i] = int(numbers_list[i])

while len(numbers_list) > 0:
    counter += 1

    if counter % k == 0:
        result_list.append(numbers_list.pop(index))
    elif counter % k != 0:
        index += 1

    if index >= len(numbers_list):
        index = 0


for i in range(0, len(result_list)):
    result_list[i] = str(result_list[i])

print(f'[{','.join(result_list)}]')
