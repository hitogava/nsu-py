def flatten(currentlist):
    res = []
    for el in currentlist:
        if isinstance(el, list):
            res.extend(flatten(el))
        else:
            res.append(el)
    return res
