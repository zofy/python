def add_numbers():
    numbers = raw_input('Write numbers in a row, please!')
    number_list = []
    num = ''
    for x in numbers:
        if x in '0123456789':
            num += x
        else:
            try:
                int(num)
            except TypeError:
                pass
            else:
                number_list.append(int(num))
                num = ''
    if num != '':
        number_list.append(num)
    return sum(number_list)


def add_numbers2():
    numbers = raw_input('Write integers in a row, please!')
    num_idxs = [i for i, x in enumerate(numbers) if x in '0123456789']
    num = ''
    output = []
    for i, x in enumerate(numbers):
        if i in num_idxs:
            num += x
        else:
            if num != '':
                output.append(int(num))
                num = ''
    if num != '':
        output.append(int(num))
    return sum(output)


print add_numbers2()

