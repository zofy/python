from random import randint, choice


def create_password_generator(sequence):
    def func(n):
        return ''.join([sequence[randint(0, len(sequence) - 1)] for x in xrange(n)])

    return func


def create_password_generator2(sequence):
    def func(n):
        output = ''
        for x in xrange(n):
            output += sequence[randint(0, len(sequence) - 1)]
        return output

    return func


def create_password_generator3(sequence):
    def func(n):
        return ''.join([choice(sequence) for x in xrange(n)])

    return func


def create_password_generator4(sequence):
    return lambda n: ''.join([choice(sequence) for x in xrange(n)])


alpha_password = create_password_generator4('abcdef')
cartoon_password = create_password_generator4('!@#$%%')
print(alpha_password(5))
print(cartoon_password(5))
print(alpha_password(10))
print(cartoon_password(10))
