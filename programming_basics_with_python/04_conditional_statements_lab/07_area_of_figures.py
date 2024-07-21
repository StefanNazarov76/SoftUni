from math import pi

figure = input()

if figure == 'square':
    a = float(input())

    print(a * a)
elif figure == 'rectangle':
    a = float(input())
    b = float(input())

    print(a * b)
elif figure == 'circle':
    r = float(input())

    print(pi * r * r)
elif figure == 'triangle':
    b = float(input())
    h = float(input())

    print((b * h) / 2)
