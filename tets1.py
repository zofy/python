'''
    Numbers = data type (float,integer,double)
    Strings = data type, sequense of characters
    Lists = sort of array, supports diff tyoes and methods
    Tuples = sort fo array, not manz methods, immutable
    Dictionary = sort of a map, key and vlaue, many data types
'''

x = ((100.25*4 + 10 - 34)/2)**2

print(x)

print(2/3) # divison: 0, import fro future div and then the result will be: 0.6666

s = 'hello'
print(s[1])
print(s[::-1])
print(s[len(s)-1::-1])

print(s[len(s)-1])
print(s[4])

list = []
for i in range(0,3,1):
    list.append(0)
print(list)
l = [0]*3
print(l)
l2 = [0, 0, 0]

l = [1,2,[3,4,'hello']]
l[2][2] = 'goodbey'
print(l)

l = [3,4,5,5,6]
l.sort()
sorted(l)
print(l)

d = {'simple_key':'hello'}
a = d['simple_key']
print(a)

d = {'k1':{'k2':'hello'}}
a = d['k1']['k2']
print(a)

d = {'k1':[{'nest_key':['this is deep',['hello']]}]}
a = d['k1'][0]['nest_key'][1][0]
print(a)

d = {'k1':[1,2,{'k2':['this is tricky',{'toughie':[1,2,['hello']]}]}]}
a = d['k1'][2]['k2'][1]['toughie'][2][0]
print(a)

l = [1,2,2,33,4,4,11,22,3,3,2]
print(set(l))


#################################

s = 'Print only the words that start with s in this sentence'
l = s.split()
for word in l:
    if word[0] == 's' or word[0] == 'S':
        print(word)
#print(l)

l = [x for x in range(0,11,2)]
l = range(0,11,2)
l = [x for x in range(0,11) if x%2 == 0]
for x in range(0,11):
    if x % 2 == 0:
        print(x)
print(l)

list = [x for x in xrange(1,51) if x % 3 == 0]
list = [x for x in xrange(0,51,3) if x > 0]
print(list)

st = 'Print every word in this sentence that has an even number of letters'
l = st.split()
for word in l:
    if len(word) % 2 == 0:
        print('%s : even' % word)

for x in xrange(1,101):
    if x % 3 == 0 and x % 5 == 0:
        print('FizzBuzz')
    elif x % 3 == 0:
        print('Fizz')
    elif x % 5 == 0:
        print('Buzz')
    else:
        print(x)


st = 'Create a list of the first letters of every word in this string'
list = [x[0] for x in st.split()]
print(list)


def my_add(a, b):
    return a + b

print(my_add(1, 2))
print(my_add('huhu', 'haha'))

def greeting(Name):
    print('Hello %s' % Name)

#print('Name: ')
#greeting(raw_input())


def is_prime(num):
    if num <= 1:
        return False
    for x in xrange(2, num):
        if num - (num/x)*x == 0:
            return False
    return True

print(is_prime(2))

### Lambda expressions

def square(num):
    result = num**2
    return result

print(square(3.2))

def square(num):
    return num**2


square = lambda num: num**2

print(square(3.6))

even = lambda num: num % 2 == 0

print(even(2))

letter = lambda s: s[0]

print(letter('hello'))

rev = lambda s: s[::-1]
print(rev('hello'))

add = lambda a, b: a + b

print(add(2, 5))

add = lambda a, b : a + b

name = 'bubu'
def greet():
    #name = 'Sammy'
    def hello():
        print('Hello %s' % name)
    hello()

greet()

'''
print(len('sss'))


x = 50

def change(x):
    print 'X is: ', x
    x = 0
    print 'Now is x: ', x
change(20)
print(x)

x = 50

def func():
    global x
    print 'x is: ', x
    x = 0
    print 'x changed to: ', x


func()
print 'x after func: ', x

print locals()
'''

n = 2
def f():
    def p():
       print 'x is: ', n
    p()
    global n
    n = 3

f()
print n