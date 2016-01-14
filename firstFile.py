from __future__ import division
from __future__ import print_function
# Numbers
print(3/2)
print(4**0.2)

# Strings
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

# Print formatting

string = 'Dnes je {den} a zajtra je {datum}'.format(den='piatok',datum='9.1.2016');
print(string)

print('Moje meno je: %s a mam %d rokov a vazim: %.1f kg!' %('Patrik',23,77.4)) # vypis ako v C

print('Vypis stringu cez r %r!'%('STRING'))
print('Vypis stringu cez s %s!\n'%('STRING'))

s1 = 'Vypis stringu bez {p} {s}!'.format(p='%',s='STRING')
print(s1)
