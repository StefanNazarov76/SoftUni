number = int(input())

digits_list = []

for digit in str(number):
    digits_list.append(digit)

digits_list.sort(reverse=True)

for i in range(len(digits_list)):
    print(digits_list[i], end='')
