def sort(word):
    return ''.join(sorted(list(word)))


def sort2(word):
    result = []
    arr = list(word)
    while len(arr) != 0:
        min = reduce(lambda x, y: x if x < y else y, arr)
        result.append(min)
        arr.remove(min)
    return ''.join(result)


def sort3(word):
    arr = list(word)
    b = True
    while b:
        b = False
        for i in xrange(0, len(arr) - 1):
            if arr[i] > arr[i + 1]:
                b = True
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                break
    return ''.join(arr)



print(sort('mama'))
print(sort3('cba'))


