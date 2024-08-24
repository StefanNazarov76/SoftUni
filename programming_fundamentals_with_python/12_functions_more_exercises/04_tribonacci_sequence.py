def tribonacci_sequence(number):
    sequence = [1, 1, 2]

    if 1 <= number <= 3:
        return sequence[:number]

    rotations = number - len(sequence)
    for _ in range(rotations):
        current_numbers = sequence[-3:]
        sequence.append(sum(current_numbers))

    return sequence


n = int(input())
result = tribonacci_sequence(n)
print(*result, sep=' ')