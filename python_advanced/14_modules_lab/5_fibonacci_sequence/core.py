def create_sequence(number):
    sequence = [0, 1]

    for _ in range(number - 2):
        next_number = sequence[-1] + sequence[-2]
        sequence.append(next_number)

    return sequence


def locate_number(number, sequence):
    try:
        index = sequence.index(number)
        return f'The number - {number} is at index {index}'

    except ValueError:
        return f'The number {number} is not in the sequence'