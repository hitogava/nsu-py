import functools


def coroutine(func):
    @functools.wraps(func)
    def wrapper():
        ret = func()
        next(ret)
        return ret
    return wrapper


@coroutine
def storage():
    values = set()
    was_there = False
    while True:
        val = yield was_there
        was_there = val in values
        if not was_there:
            values.add(val)


st = storage()
print(st.send(10))
print(st.send(4))
print(st.send(4))
