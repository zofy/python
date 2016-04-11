d = {'adam': 1, 'eve': 2, 'peter': 3}


def flip(d):
    output = {}
    for k in d:
        output[d[k]] = k
    return output


def flip2(d):
    return {t[1]: t[0] for t in d.items()}


def flip3(d):
    return {value: key for key, value in d.items()}


print(flip(d))
