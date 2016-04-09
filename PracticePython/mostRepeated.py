from collections import Counter
from Crypto.Cipher import AES



def show(list):
    max = 0
    for word in list:
        for letter in set(word):
            if word.count(letter) > max:
                max_words = {}
                max = word.count(letter)
                max_words[word] = max
            elif word.count(letter) == max:
                max_words[word] = max
    return max_words


def show2(list):
    return sorted(list, key=lambda word: map(lambda letter: word.count(letter), set(word)))[-1]


def show3(list):
    return reduce(lambda a, b: a if Counter(a).most_common()[0][1] > Counter(b).most_common()[0][1] else b, list)


def show4(list):
    word_counts = {word: max(Counter(word).items(), key=lambda t: t[1]) for word in list}
    return max(word_counts, key=lambda word: word_counts[word][1])


line = 'This isiss aa test program'
print(show4(line.split()))


def once_again(list):
    d = {word: max(Counter(word).items(), key=lambda t: t[1]) for word in list}
    return max(d, key=lambda word: d[word][1])

# print(once_again(line.split()))
# print(show2(line.split()))


def cc(list):
    return [map(lambda letter: word.count(letter), set(word)) for word in list]

print(cc(line.split()))
