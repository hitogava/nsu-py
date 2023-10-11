def flatten(currentlist, currentdepth, depth=0):
    res = []
    for el in currentlist:
        res += flatten(el,currentdepth+1,depth) if isinstance(el,list) and currentdepth < depth else [el]
    return res
