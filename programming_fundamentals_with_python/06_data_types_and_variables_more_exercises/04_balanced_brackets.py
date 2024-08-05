lines = int(input())
brackets = 0

for _ in range(lines):
    current_symbol = input()
    if current_symbol == '(':
        brackets += 1
    elif current_symbol == ')':
        brackets -= 1
    if brackets != 0 and brackets != 1:
        print('UNBALANCED')
        break
else:
    print('BALANCED')
