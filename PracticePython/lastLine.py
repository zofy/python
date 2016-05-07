file_name = str(raw_input('Name some file please: '))
path = 'C:/Users/Patrik/Desktop/' + file_name


def print_last_line():
    with open(path, 'r') as f:
        print f.readlines()[-1]


def print_last_line2():
    with open(path, 'r') as f:
        l = f.readline()
        while l:
            line, l = l, f.readline()
        print line


#  the best solution for real cases
def print_last_line3():
    with open(path, 'r') as f:
        for line in f:
            pass
        print line


#  even little bit better
def print_last_line4():
    for line in open(path, 'r'):
        pass
    print line


print_last_line4()
