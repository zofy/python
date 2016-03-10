def sum_arguments(*args):
    output = None
    for x in args:
        if output is None:
            output = x
        else:
            output += x
    return output


def sum_arguments2(*args):
    if not args:
        return args
    output = type(args[0])()
    for x in args:
        output += x
    return output


print(sum_arguments2())

print(type(3.14)())