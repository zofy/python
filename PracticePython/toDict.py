path = 'C:/Users/Patrik/Desktop/passw.txt'


def convert():
    output = {}
    with open(path, 'r') as f:
        for line in f:
            l = line.strip().split(':')
            if l[0][0] != '#':
                output[l[0]] = l[2]
        keys = sorted(output.keys())
        for k in keys:
            print(k + ': ' + output[k])
    return output


def convert2():
    with open(path, 'r') as f:
        for l in sorted(f.readlines(), key=lambda line: line.strip().split(':')[0]):
            result = l.strip().split(':')
            print(result[0] + ': ' + result[2])


convert2()
