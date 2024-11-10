class dictionary_iter:
    def __init__(self, dictionary: dict) -> None:
        self.dictionary = list(dictionary.items())
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.dictionary) - 1:
            self.index += 1
            dictionary = self.dictionary[self.index]
            return dictionary
        raise StopIteration


result = dictionary_iter({1: '1', 2: '2'})
for x in result:
    print(x)
