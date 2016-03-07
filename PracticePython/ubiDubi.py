s = {'a', 'e', 'i', 'o', 'u', 'y'}


def translate(word):
    idx_list = [i for i, l in enumerate(word) if l in s]
    result = list(word)
    j = -1
    for i in idx_list:
        if j == -1:
            j = i
        if i-j != 1:
            result[i] = 'ub' + result[i]
        j = i
    return ''.join(result)

print(translate('yathon'))

print(zip(['ub'], []))