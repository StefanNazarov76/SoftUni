from collections import deque

input_line = input()
customers = deque()

while input_line != 'End':
    if input_line != 'Paid':
        customers.append(input_line)
    else:
        while customers:
            print(customers.popleft())
    input_line = input()

print(f'{len(customers)} people remaining.')
