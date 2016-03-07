def sum_arguments(*args):
    output = None
    for x in args:
        if output is None:
            output = x
        else:
            output += x
    return output


print(sum_arguments([1,2], [3,4]))