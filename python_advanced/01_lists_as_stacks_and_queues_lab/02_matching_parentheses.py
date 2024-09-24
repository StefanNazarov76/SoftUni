expression = input()

parentheses_indexes = []

for index in range(len(expression)):
    if expression[index] == '(':
        parentheses_indexes.append(index)
    elif expression[index] == ')':
        start = parentheses_indexes.pop()
        end = index + 1
        print(expression[start:end])
