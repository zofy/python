s = {'a', 'e', 'i', 'o', 'u'}


def hash_word(word):
    if word[0] in s:
        return word + 'way'
    return word[1:] + word[0] + 'ay'


def translate2(line):
    return ' '.join(map(hash_word, line.split()))


line = 'this is a test translation'
print(translate2(line))