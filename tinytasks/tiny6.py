def flatten(currentlist):
    res = []
    for el in currentlist:
        if isinstance(el, list):
            for k in flatten(el):
                res.append(k)
        else:
            res.append(el)
    return res
