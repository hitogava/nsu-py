class MyIterator:
    def __init__(self, iterables):
        self.iterables = iterables
        self.currElementIndex = 0
        self.currIterableIndex = 0

    def __next__(self):
        if self.currElementIndex == len(self.iterables[self.currIterableIndex]):
            self.currElementIndex = 0
            if (self.currIterableIndex + 1) == len(self.iterables):
                raise StopIteration
            self.currIterableIndex += 1

        self.currElementIndex += 1

        return self.iterables[self.currIterableIndex][self.currElementIndex - 1]

    def __iter__(self):
        return self


def chain(*iterables):
    return MyIterator(iterables)


my_list = ("a", "b")
print(list(chain([1, 2, 3, 5, 6], [2, 2, 8], my_list)))
