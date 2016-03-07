def showFirstLast(sequence):
    return sequence[:1] + sequence[-1:]


def showFirstLast2(sequence):
    return sequence[0:len(sequence):len(sequence) - 1]


print(showFirstLast([1, 2, 3]))

l = [1,2,3]
d = [4,5,6]
s = l + d
print(s)