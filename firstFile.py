from __future__ import division
from __future__ import print_function
print(3/2)
print(4**0.2)

s = 'hahaha'

print(s[2:3])
print(s[-1])
print(s[:-2])
print(s[::-1])
print(len(s))
print(s.upper())
print(s.lower())
print(s.islower())
print(s.isupper())

list = s.split('s')
print(list)
# print formatting

s = 'Patrik'
print('Toto je: ',s)
#print 'Toto je %s' %s # pre python 2

print('Hi ' + s + ' how are you?')