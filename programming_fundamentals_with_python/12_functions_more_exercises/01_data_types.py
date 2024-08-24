def read_input(data_type):
    final_data = None

    if data_type == 'int':
        input_data = int(input())
        final_data = input_data * 2
    elif data_type == 'real':
        input_data = float(input())
        final_data = f'{input_data * 1.5:.2f}'
    elif data_type == 'string':
        input_data = input()
        final_data = f'${input_data}$'

    return final_data


input_type = input()
data = read_input(input_type)

print(data)
