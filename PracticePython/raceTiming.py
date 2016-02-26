
def calculate():
    time = 0
    i = 0
    while True:
        t = raw_input('Enter 10km run time: (q to exit)')
        if t == 'q':
            break
        else:
            i += 1
            time += float(t)
    if i == 0:
        return 0
    return time/float(i)

print(calculate())
