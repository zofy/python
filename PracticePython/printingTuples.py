people = [('Barack', 'Obama', 7.85), ('Vladimir', 'Putin', 3.626), ('Jinping', 'Xi', 10.603), ('Baraxk', 'Obama', 7.85)]


def print_people(list):
    return '\n'.join(
            [person[1].ljust(11) + person[0].ljust(11) + '{0:.2f}'.format(person[2]).ljust(5) for person in people])


def print_people2(list):
    list_sorted = sorted(list, key=lambda t: t[1] + ' ' + t[0])
    return '\n'.join(['{:10s} {:10s} {:5.2f}'.format(record[1], record[0], record[2]) for record in list_sorted])


def print_people3(list):
    list_sorted = sorted(list, key=lambda t: t[1] + ' ' + t[0])
    return '\n'.join(['{1:10s} {0:10s} {2:5.2f}'.format(*record) for record in list_sorted])


def print_people4(list):
    list_sorted = sorted(list, key=lambda t: (t[1], t[0]))
    return '\n'.join(['{1:10s} {0:10s} {2:5.2f}'.format(*record) for record in list_sorted])

print(print_people4(people))
