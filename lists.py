my_list = [1, 2, 3, 4]

print(my_list, len(my_list))

my_list = ['mama', 1, 4, 'tata', 'o']

print(my_list, len(my_list))

print(my_list[:4])
print(my_list[1:])
print(my_list[:]*2)

my_list2 = my_list + ['mama', 'tata']
print(my_list2)

l = [1, 2, 45]
l.append('bubu')
print(l)

x = l.pop()
print(x)

x = l.pop(0)
print(x)

print(l)
print(l.count(45))

l.sort()
print(l)

l = ['a', 'c', 'x', 'b']
l.sort()
print(l)

l.sort(reverse=True)
print(l)

l.reverse()
print(l)

l_1 = [1, 2, 3]
l_2 = [4, 5, 6]
l_3 = [7, 8, 9]
matrix = [l_1, l_2, l_3]

print(matrix)
print(matrix[0])
print(matrix[0][0])
print(matrix[1][1])
print(matrix[2][0])

first_col = [row[0] for row in matrix]
print(first_col)
sec_col = [row[1] for row in matrix]
sec_row = [n for n in matrix[1]]
print(sec_row)