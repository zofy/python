def xml_generator(tag, val='', **kwargs):
    return '<' + str(tag) + ''.join(
        [' ' + str(k) + '=' + '"' + str(kwargs[k]) + '"' for k in kwargs]) + '>' + val + '</' + str(
        tag) + '>'


print xml_generator('foo', 'bar', a=1, b=2)
