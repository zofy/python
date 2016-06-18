def transform(func, d):
    keys = [k for k in d]
    values = [d[k] for k in keys]
    new_vals = map(func, values)
    return {k: new_vals[i] for i, k in enumerate(keys)}


d = {'a': 1, 'b': 2, 'c': 3}
print transform(lambda x: x**2, d)
