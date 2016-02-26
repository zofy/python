

def mysum(*args):
    sum = 0
    for x in args:
        print(x)
        # sum += x
    print(sum)
    return sum

mysum(*[1,2,'e'])
