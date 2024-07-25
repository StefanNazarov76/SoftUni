from sys import maxsize

n = int(input())

odd_sum = 0
odd_min = maxsize
odd_max = - maxsize

even_sum = 0
even_min = maxsize
even_max = - maxsize

for i in range(1, n + 1):
    num = float(input())

    if i % 2 == 0:
        even_sum += num
        if num < even_min:
            even_min = num
        if num > even_max:
            even_max = num
    else:
        odd_sum += num
        if num < odd_min:
            odd_min = num
        if num > odd_max:
            odd_max = num

if n == 0:
    print(f'OddSum={odd_sum:.2f},')
    print(f'OddMin=No,')
    print(f'OddMax=No,')
    print(f'EvenSum={even_sum:.2f},')
    print(f'EvenMin=No,')
    print(f'EvenMax=No')
elif n == 1:
    print(f'OddSum={odd_sum:.2f},')
    print(f'OddMin={odd_min:.2f},')
    print(f'OddMax={odd_max:.2f},')
    print(f'EvenSum={even_sum:.2f},')
    print(f'EvenMin=No,')
    print(f'EvenMax=No')
else:
    print(f'OddSum={odd_sum:.2f},')
    print(f'OddMin={odd_min:.2f},')
    print(f'OddMax={odd_max:.2f},')
    print(f'EvenSum={even_sum:.2f},')
    print(f'EvenMin={even_min:.2f},')
    print(f'EvenMax={even_max:.2f}')
