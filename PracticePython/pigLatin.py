s = {'a', 'e', 'i', 'o', 'u'}


def hash_word(word):
    if word[0] in s:
        return word + 'way'
    return word[1:] + word[0] + 'ay'


print(hash_word('eat'))
