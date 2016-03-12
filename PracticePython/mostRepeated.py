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
    return sorted(list, key=lambda word: map(lambda letter: word.count(letter), set(word)))


line = 'This isiss aa test program'
print(show2(line.split()))
