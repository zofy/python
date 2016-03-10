import string
from math import pi
from string import find

import time


def vol(rad):
    return (4.0/3)*pi*rad**3

print('Volume of a sphere is: %s' % vol(3))


def ran_bool(num, low, high):
    return num <= high and num >= low


def ran_check(num, low, high):
    pass


def up_low(string):
    up = 0
    low = 0
    for letter in string:
        if ord(letter) >= 65 and ord(letter) <= 90:
            up += 1
        elif ord(letter) >= 97 and ord(letter) <= 122:
            low += 1
    print 'No. of upper: ', up
    print 'No. of lower: ', low
    return up, low

#up_low('Hello Mr. Rogers, how are you this fine Tuesday?')


def up_low2(str):
    up = 0
    low = 0
    lcase = string.ascii_lowercase
    ucase = string.ascii_uppercase
    for letter in str:
        if find(ucase, letter) >= 0:
            up += 1
        elif find(lcase, letter) >= 0:
            low += 1
    print 'No. of upper: ', up
    print 'No. of lower: ', low
    return up, low


def up_low3(str):
    up = 0
    low = 0
    for letter in str:
        if letter.isupper():
            up += 1
        elif letter.islower():
            low += 1
    print 'No. of upper: ', up
    print 'No. of lower: ', low
    return up, low

up_low3('Hello Mr. Rogers, how are you this fine Tuesday?')


def unique_list(l):
    list = []
    for x in l:
        if list.count(x) == 0:
            list.append(x)
    return list

print(unique_list([5,1,2,2,3,1,1,1,1]))


def multiply(numbers):
    if len(numbers) == 0:
        return -1
    result = numbers[0]
    for x in numbers:
        result = result*x
    return result

print(multiply([1,2,1,1]))


def palindrome(s):
    return s[::-1] == s


def palindrome2(s):
    str = s[::-1]
    for x in xrange(0, len(str)):
        if str[x] != s[x]:
            return False
        else:
            return True


print(palindrome2('helleh'))


def is_pangram(s):
    abc = [0]*26
    idx = 0
    for letter in s:
        idx = ord(letter.upper())
        if idx >= 65 and idx <= 90:
            abc[idx - 65] = 1
    return abc.count(1) == len(abc)


def is_pal(s):
    abc = string.ascii_lowercase
    return set(abc) <= set(s.lower())

print(is_pal('The quick brown fox jumps over the lazy dog'))
