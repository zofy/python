d = {'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15}


def convert(hex):
    l = [x for x in str(hex)]
    return sum([d[a.lower()] * 16 ** i if a.isalpha() else int(a) * 16 ** i for i, a in enumerate(l[::-1])])


while True:
    num = str(raw_input('Input some hex-number: (q - quit)'))
    if num == 'q':
        break
    print(convert(num))
