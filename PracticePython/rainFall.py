def insert():
    d = {}
    input_city = str(raw_input('Insert city: '))
    while input_city != '':
        input_rain = float(raw_input('Rain[mm]: '))
        d.setdefault(input_city, 0)
        d[input_city] += input_rain
        input_city = str(raw_input('Insert city: '))
    for city in d:
        print('{:10} {:5.2f}'.format(city, d[city]))


def insert2():
    d = {}
    input_city = str(raw_input('Insert city: '))
    while input_city:
        input_rain = float(raw_input('Rain[mm]: '))
        d[input_city] = d.get(input_city, 0) + input_rain
        input_city = str(raw_input('Insert city: '))
    for city in d:
        print('{:10}: {:5.2f}'.format(city, d[city]))


insert2()
