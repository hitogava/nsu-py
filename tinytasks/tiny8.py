import functools


def deprecated(f=None, since=None, will_be_removed=None):
    if f is None:
        return functools.partial(deprecated,
                                 since=since,
                                 will_be_removed=will_be_removed)

    def inner(*args, **kwargs):
        dep_msg = f"Warning: function {f.__name__} is deprecated"
        if since is not None:
            dep_msg += f" since version {since}"
        dep_msg += "."
        dep_msg += " It will be removed in "

        if will_be_removed is not None:
            dep_msg += f"version {will_be_removed}"
        else:
            dep_msg += "future versions"

        print(dep_msg)
        ret = f(*args, **kwargs)
        return ret

    return inner


@deprecated(since="1.2.0", will_be_removed="1.2.3")
def foo():
    print('Hello from foo')


foo()
