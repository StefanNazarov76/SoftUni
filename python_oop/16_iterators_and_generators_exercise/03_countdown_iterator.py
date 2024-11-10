class countdown_iterator:
    def __init__(self, count: int) -> None:
        self.count = count
        self.current_number = count + 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_number > 0:
            self.current_number -= 1
            return self.current_number
        raise StopIteration


iterator = countdown_iterator(10)
for item in iterator:
    print(item, end=" ")
