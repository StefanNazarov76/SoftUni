class take_skip:
    def __init__(self, step: int, count: int) -> None:
        self.step = step
        self.count = count
        self.counter = 0
        self.current_number = -step

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter < self.count:
            self.counter += 1
            self.current_number += self.step
            return self.current_number
        raise StopIteration


numbers = take_skip(10, 5)
for number in numbers:
    print(number)
