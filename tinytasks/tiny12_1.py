def take(seq, n):
    res = []
    for i in range(n):
        try:
            res.append(next(seq))
        except StopIteration:
            break
    return res


def cycle(iterable):
    visited = []
    for i in iterable:
        yield i
        visited.append(i)
    while True:
        yield from visited


print(take(cycle([1, 2, 3]), 6))