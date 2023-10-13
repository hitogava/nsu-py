def flatten(currentlist, currentdepth, depth=0):
    res = []
    for el in currentlist:
        if isinstance(el, list) and currentdepth < depth:
            for k in flatten(el, currentdepth+1, depth):
                res.append(k)
        else:
            res.append(el)
    return res
