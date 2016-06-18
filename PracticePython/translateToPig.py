import pigLatin

file = 'C://Users/Patrik/Desktop/test.txt'


def translate(text_file):
    with open(text_file, 'r') as f:
        return [pigLatin.hash_word(word) for line in f.readlines() for word in line.split()]


def translate2(text_file):
    with open(text_file, 'r') as f:
        l = f.readline()
        output = []
        while l:
            for word in l.split():
                output.append(pigLatin.hash_word(word))
            l = f.readline()
    return output


print translate2(file)
