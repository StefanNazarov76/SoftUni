from typing import List


class vowels:
    def __init__(self, string: str):
        self.string = string
        self.index: int = -1
        self.vowels_in_string: List = [c for c in string if c.lower() in 'aeiuyo']

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index < len(self.vowels_in_string):
            return self.vowels_in_string[self.index]
        raise StopIteration


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
