# d = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 3}
d = {"Ivanov": 97832, "Petrov": 55521, "Kuznecov": 97832}
new_d = {}
for item in d.items():
    if (item[1] in new_d):
        new_d[item[1]].append(item[0])
    else:
        new_d[item[1]] = [item[0]]
print(new_d)
