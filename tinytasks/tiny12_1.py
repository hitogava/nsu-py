def take(seq, n):
    res = []
    for i in range(n):
        try:
            res.append(next(seq))
        except StopIteration:
            break
    return res


class MyIterator:
    def __init__(self, collection):
        self.collection = collection
        self.currIndex = 0

    def __next__(self):
        self.currIndex = (self.currIndex + 1) % len(self.collection)
        return self.collection[self.currIndex - 1]


def cycle(elems):
    return MyIterator(elems)


print(take(cycle([1, 2, 3]), 4))
