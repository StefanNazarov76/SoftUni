stack = []

for _ in range(int(input())):
    command = input().split()

    if command[0] == '1':
        stack.append(command[1])
    elif command[0] == '2' and stack:
        stack.pop()
    elif command[0] == '3' and stack:
        print(max(stack))
    elif command[0] == '4' and stack:
        print(min(stack))

print(*stack, sep=', ')
