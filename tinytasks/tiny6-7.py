def flatten(currentlist, currentdepth, depth=3):
    res = []
    for el in currentlist:
        res += flatten(el,currentdepth+1) if isinstance(el,list) and currentdepth < depth else [el]
    return res
a = [1, 2, [4, 5], [6, [7]], [[[8]]]]
print(flatten(a,0))
