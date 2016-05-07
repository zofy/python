import glob


def find_longest(dir):
    try:
        files = glob.glob('C:\Users\Patrik\Desktop\\' + str(dir) + '\*.txt')
    except Exception:
        print 'No such a directory!'
    else:
        output = {}
        for file in files:
            file_name = file.split('\\')[-1]
            longest = ''
            for line in open(file):
                list = sorted(line.split(), key=lambda word: len(word))
                if len(list) == 0:
                    continue
                l_word = list[-1]
                if len(l_word) > len(longest):
                    longest = l_word
                    output[file_name] = longest
        print output


def find_longest2(dir):
    try:
        files = glob.glob(str(dir) + '*.txt')
    except:
        print 'Cannot find or open any file'
    else:
        output = {}
        for file in files:
            file_name = file.split('\\')[-1]
            longest = ''
            for line in open(file):
                list = sorted(line.split(),
                              key=lambda word: len([x for x in word if 97 <= ord(x) <= 122 or 65 <= ord(x) <= 90]))
                if list == []:
                    continue
                l_word = list[-1]
                if l_word > longest:
                    longest = l_word
                    output[file_name] = l_word
        print output


# find_longest('Test')
find_longest2('C:\Users\Patrik\Desktop\Test\\')
