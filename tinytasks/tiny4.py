# d = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 3}
d = {"Ivanov": 97832, "Petrov": 55521, "Kuznecov": 97832}
# d = {"Ivanov": 97832, "Petrov": 55521, "Kuznecov": 97835}
new_d = {}
for value in set(d.values()):
    keys = tuple([k for k in d.keys() if d[k] == value])
    new_d[value] = keys if len(keys) > 1 else keys[0]
print(new_d)
