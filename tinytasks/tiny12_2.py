def chain(*iterables):
    for i in iterables:
        yield from i


my_list = ("a", "b")
print(list(chain([1,2,3, 5, 6], [2,2,8], my_list)))
s = {1, 2, 3}
print(list(chain(s, [1,2,3, 5, 6], [2,2,8], my_list)))
