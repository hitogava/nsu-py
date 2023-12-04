def take(seq, n):
    res = []
    for i in range(n):
        try:
            res.append(next(seq))
        except StopIteration:
            break
    return res


def cycle(iterable):
    while True:
        yield from iterable


print(take(cycle([1, 2, 3]), 10))