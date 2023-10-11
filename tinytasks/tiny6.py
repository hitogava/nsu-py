def flatten(currentlist):
    res = []
    for el in currentlist:
        res += flatten(el) if isinstance(el,list) else [el]
    return res
