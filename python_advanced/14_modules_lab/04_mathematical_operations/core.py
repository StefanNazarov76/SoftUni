sign_mapper = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y,
    '^': lambda x, y: x ** y,
}


def execute_expression(exp):
    num1, sign, num2 = exp.split()
    num1 = float(num1)
    num2 = int(num2)

    return sign_mapper[sign](num1, num2)
