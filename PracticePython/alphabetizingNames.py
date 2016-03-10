people = [{'first': 'Rauven', 'last': 'Lerner', 'email': 'reuven@lerner.co.il'},
          {'first': 'Barack', 'last': 'Obama', 'email': 'president@whitehouse.gov'},
          {'first': 'Vladimir', 'last': 'Putin', 'email': 'president@kremvax.ru'}]


def sort(list):
    b = 1
    while b:
        b = 0
        for i in xrange(0, len(list) - 1):
            if list[i]['last'] + list[i]['first'] > list[i + 1]['last'] + list[i + 1]['first']:
                b = 1
                list[i], list[i + 1] = list[i + 1], list[i]
                break
        for person in list:
            print(person['last'] + ', ' + person['first'] + ': ' + person['email'])
    return list


def getKey(item):
    return item[0]


def sort2(list):
    l = sorted([(person['last'] + ', ' + person['first'], person['email']) for person in list], key=getKey)
    return '\n'.join([': '.join(p) for p in l])


# sort(people)
print(sort2(people))
# print('lbama' < 'lerner')
