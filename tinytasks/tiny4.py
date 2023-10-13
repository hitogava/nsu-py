new_d = {}
for value in set(d.values()):
    keys = tuple([k for k in d.keys() if d[k] == value])
    new_d[value] = keys if len(keys) > 1 else keys[0]
