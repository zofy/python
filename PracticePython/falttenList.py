def flatten(list):
    return [a for x in list for a in x]


print flatten([[1, 2], [3, 4]])
