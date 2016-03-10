from sys import argv


def funct(*args):
    first, second = args
    print("Arguments %s and %s are being printed!" % (first, second))


def funct2(name, surname):
    print("Your name: %s and surname: %s." % (name, surname))


x = 1
y = 33
funct(x, y)

'''
print("Ypur Fisrt name:")
name = raw_input()
print("Ypur Second name:")
surname = raw_input()
funct2(name, surname)

script, f = argv

file = open(f)


def print_file(file):
    print(file.read())


def rewind(file):
    file.seek(0)


def print_line(line,file):
    print line, file.readline()


print_file(file)
rewind(file)

cur_line = 1
print_line(cur_line, file)
print_line(cur_line + 1, file)
print_line(cur_line + 1, file)

file.close()
'''


def f(weight):
    try:
        float(weight)
    except:
        TypeError
    else:
        weight = float(weight)
        print('Your weight is: %.2f' % weight)

#weight = float(raw_input())

#f(weight=raw_input())

list = [1,2,3,4,5]

def sum(list):
    sum = 0
    for i in range(0, len(list), 1):
        sum += list[i]
    return sum

print(sum(list))

t = ((1,2),(3,4,3),(5,6))
for tuple in t:
    if tuple.__len__() < 3:
        print(tuple)

tuple = (1,2,3,4)

# Dedenie od tuple a prepisanie metody __len__
class tt(tuple.__class__):
    def __len__(void):
        return 1

t = tt((1,2,3,4))

print(t.count(1))

d = {1:'a', 2:'b', 3:'c'}

for k,v in d.items():
    print("Key is: %s, Value is: %s" % (k, v))

for n in d:
    print('Keys: %s, Values: %s' % (n, d[n]))
    #print("Key is: %s, Value is: %s" % (k, v))

# while loops
'''
meno = 'Pato'
while meno.__eq__('Pato'):
    print('Yes!')
    print('Enter name:')
    meno = raw_input()
else:
    print('No longer!')
'''
x = 0
while x<10:
    if(x == 5):
        x += 1
        continue
    print(x)
    x += 1

x = xrange(1,6)
y = range(1,6)
if not type(x).__eq__(type(y)):
    print('They are not the same!')

if type(x) is not type(y):
    print('huhu')

print(type(x))


# List comprehension

l = [x**2 for x in xrange(0,4)]
print(l)

l = [x for x in xrange(0,11) if x % 2 == 0]
print(l)

l = []
for x in xrange(0,11):
    if(x%2 == 0):
        l.append(x)

print(l)

# convert C to F
print('Insert temperatures: ')
celsius = ['%.2f' % (float(raw_input())*(9/5.0) +32) for t in xrange(0,5)]
print(celsius)

#fahrenheit = [(float(t)*()) for t in celsius]
#print(fahrenheit)