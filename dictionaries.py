dict = {'k1': 11, 'k2': 'bubu', 'k3': 3.78}

print(dict['k2'][::-1])

dict['k1'] += 33
dict['k2'] = dict['k2'][:3]
dict['k3'] -= 2
dict['k1'] /= 2

print(dict['k1'], dict['k2'], "%.2f" %dict['k3'])

d =  {1: [11, 34, 'ggg'], 2: 'bubu', 3: 3.78}
d[1].pop()
d[1].append('huhuhahah')
print(d[1][2])

d = {}
d['animals'] = ['dog', 'cat', 'mouse', 'rat']
d['moods'] = ['happy', 'neutral', 'sad', 'excited']

print('Thats a %s %s!' % (d['moods'][0], d['animals'][3]))

#d = {[1, 2, 3]: 'haha'}

##### Tuples

t = (1, 1, 2.3456, '34t')
print(t[2])

l = [1, 1, 2, 3]

l.count(1)
t.count(1)

f = open('test.txt')
#ret = f.readline()
l = []
for line in open('test.txt'):
    l.append(line)

# watch the difference
list = []
for line in f.readline():
    list.append(line)
print(list)

# zapis do suboru
w = open('write.txt', 'w+')

#for line in open('test.txt'):
#    w.write(line)

o = open('test.txt')
for line in o:
    for spell in line:
        w.write(spell)
        if spell != '\n':
            w.write(' ')

# SET
x = set()

x.add(1)
x.add('efe')
x.add('efed')
print(x)

l = [1, 1, 1, 1, 3, 2, 3, 2, 5]
t = (1, 1, 1, 1, 3, 2, 3, 2, 5)
x.add(t)

y = set()

for n in l:
    y.add(n)
print(y)

