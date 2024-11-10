from typing import List


def get_primes(integers: List):
    for digit in integers:
        if digit > 1:
            for num in range(2, digit):
                if digit % num == 0:
                    break
            else:
                yield digit


print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))
