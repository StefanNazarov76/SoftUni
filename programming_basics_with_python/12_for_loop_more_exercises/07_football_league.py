stadium_capacity = int(input())
fans_count = int(input())

a = 0
b = 0
v = 0
g = 0

for _ in range(fans_count):
    sector = input()

    if sector == 'A':
        a += 1
    elif sector == 'B':
        b += 1
    elif sector == 'V':
        v += 1
    elif sector == 'G':
        g += 1

a_percentage = (a / fans_count) * 100
b_percentage = (b / fans_count) * 100
v_percentage = (v / fans_count) * 100
g_percentage = (g / fans_count) * 100
capacity_percentage = (fans_count / stadium_capacity) * 100

print(f'{a_percentage:.2f}%')
print(f'{b_percentage:.2f}%')
print(f'{v_percentage:.2f}%')
print(f'{g_percentage:.2f}%')
print(f'{capacity_percentage:.2f}%')
