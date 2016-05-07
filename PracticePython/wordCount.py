def count_words(file):
    chars = 0
    words = 0
    lines = 0
    u_words = set()
    with open(file, 'r') as f:
        for line in f:
            lines += 1
            word_list = line.split()
            words += len(word_list)
            u_words.update(set(word_list))
            chars += len(line)
    print 'Number of chars %s' % str(chars)
    print 'Number of words %s' % str(words)
    print 'Number of lines %s' % str(lines)
    print 'Number of unique words %s' % str(len(u_words))


def count_words2(file):
    chars = 0
    words = 0
    u_words = set()
    for lines, line in enumerate(open(file, 'r'), 1):
        word_list = line.split()
        words += len(word_list)
        u_words.update(set(word_list))
        chars += len(line)
    print 'Number of chars %s' % str(chars)
    print 'Number of words %s' % str(words)
    print 'Number of lines %s' % str(lines)
    print 'Number of unique words %s' % str(len(u_words))

# file_name = 'C://Users/Patrik/Desktop/' + str(raw_input('Input name of the file, please: '))
file_name = 'C://Users/Patrik/Desktop/test-file.txt'
count_words2(file_name)