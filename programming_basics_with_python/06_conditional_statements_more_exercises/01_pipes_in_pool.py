volume = int(input())
pipe_one_debit = int(input())
pipe_two_debit = int(input())
hours = float(input())

liters_from_pipe_one = pipe_one_debit * hours
liters_from_pipe_two = pipe_two_debit * hours

total_liters = liters_from_pipe_one + liters_from_pipe_two

fill_percentage = (total_liters / volume) * 100
pipe_one_percentage = (liters_from_pipe_one / total_liters) * 100
pipe_two_percentage = (liters_from_pipe_two / total_liters) * 100

if volume >= total_liters:
    print(f'The pool is {fill_percentage:.2f}% full. Pipe 1: {pipe_one_percentage:.2f}%.'
          f' Pipe 2: {pipe_two_percentage:.2f}%.')
else:
    overflow = total_liters - volume
    print(f'For {hours:.2f} hours the pool overflows with {overflow:.2f} liters.')
