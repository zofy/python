def join(numbers):
    return ','.join([str(num) for num in numbers])

l = range(10)
print join(l)
