steps = input()

total_steps = 0

while steps != 'Going home':
    steps = int(steps)
    total_steps += steps

    if total_steps >= 10000:
        diff = total_steps - 10000
        print(f'Goal reached! Good job!')
        print(f'{diff} steps over the goal!')
        break

    steps = input()
else:
    steps = int(input())
    total_steps += steps
    diff = abs(total_steps - 10000)
    if total_steps >= 10000:

        print(f'Goal reached! Good job!')
        print(f'{diff} steps over the goal!')
    else:
        print(f'{diff} more steps to reach goal.')
