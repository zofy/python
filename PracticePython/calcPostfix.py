import operator

ops = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.div, '^': operator.pow}


def calc(eq):
    l = eq.split()
    return ops[l[0]](float(l[1]), float(l[2]))

print 'Example: + 1 1'
eq = '+ 1 1'
while eq != 'q':
    print calc(eq)
    eq = raw_input('Give me equation in postfix: ')


print calc('^ 2.00 2')
