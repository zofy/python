numbers = [1, 1, 1, 1, 1]


def find_out(list):
    d = {}
    for n in list:
        d.setdefault(n, 1)
    return len(d)


def find_out2(list):
    return len(set(list))


def find_out3(list):
    unique = set()
    unique.update(list)
    return len(unique)


# print(find_out([]))
print(find_out3([]))