def replace(list):
    list[:] = ['a'] * 6
    return list


l = range(10);
print(l)
replace(l)
print(l)
