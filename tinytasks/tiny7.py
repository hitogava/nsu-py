def flatten(currentlist, depth=None):
    res = []
    for el in currentlist:
        if isinstance(el, list):
            if depth is None:
                res.extend(flatten(el))
            elif depth:
                res.extend(flatten(el, depth - 1))
            else:
                res.append(el)
        else:
            res.append(el)
    return res


print(flatten([1, 2, [4, 5], [6, [7]], 8], depth=0))
print(flatten([1, 2, [4, 5], [6, [7]], 8]))
