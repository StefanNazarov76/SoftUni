class sequence_repeat:
    def __init__(self, sequence: str, number: int) -> None:
        self.sequence = sequence
        self.number = number
        self.index = -1
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter < self.number:
            self.counter += 1
            self.index += 1
            if self.index == len(self.sequence):
                self.index = 0
            return self.sequence[self.index]
        raise StopIteration


result = sequence_repeat('abc', 5)
for item in result:
    print(item, end='')
