from itertools import permutations
from typing import List


def possible_permutations(numbers: List):
    for number in permutations(numbers):
        yield list(number)


[print(n) for n in possible_permutations([1, 2, 3, 4])]
