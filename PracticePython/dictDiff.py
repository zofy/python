d1 = {'a': 1, 'b': 2, 'c': 3}
d2 = {'a': 1, 'b': 5, 'd': 4}


def diff(d1, d2):
    output = {}
    set1 = set(d1.items())
    set2 = set(d2.items())
    diff_set = set1.union(set2) - (set1 & set2)
    for item in diff_set:
        output.setdefault(item[0], [None, None])
        if output[item[0]][0] is None:
            output[item[0]][0] = item[1]
        else:
            output[item[0]][1] = item[1]
    return output


def diff2(d1, d2):
    output = {}
    set1 = set(d1.items())
    set2 = set(d2.items())
    diff_set = set1.union(set2) - (set1 & set2)
    for item in diff_set:
        output.setdefault(item[0], [])
        output[item[0]].append(item[1])
        if item[0] not in d1.keys() or item[0] not in d2.keys():
            output[item[0]].append(None)
    return output


def diff3(d1, d2):
    output = {}
    all_keys = d1.keys() + d2.keys()
    for key in all_keys:
        if d1.get(key) != d2.get(key):
            output[key] = [d1.get(key), d2.get(key)]
    return output

print(diff3(d1, d2))
