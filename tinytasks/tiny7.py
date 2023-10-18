def get_max_fold_level(l, current_level):
    if not isinstance(l,list): return current_level - 1
    return max(get_max_fold_level(x, current_level+1) for x in l)


def flatten(currentlist, depth=None):
    if depth is None:
        depth = get_max_fold_level(currentlist, 0)
    res = []
    for el in currentlist:
        if isinstance(el, list) and depth:
            res.extend(flatten(el, depth-1))
        else:
            res.append(el)
    return res
