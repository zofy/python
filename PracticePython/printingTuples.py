people = [('Barack', 'Obama', 7.85), ('Vladimir', 'Putin', 3.626), ('Jinping', 'Xi', 10.603)]


def print_people(list):
    return '\n'.join(
            [person[1].ljust(11) + person[0].ljust(11) + '{0:.2f}'.format(person[2]).ljust(5) for person in people])


print(print_people(people))
