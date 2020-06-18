#!/usr/bin/env python

print '===== 01'
a = [[0]]*5
a[0][0] = 3
a[1][0] = a[0][0] + 1
print a
print map(lambda x: id(x), a)

print '===== 02'
a = [i**2 for i in range(10) if i > 5]
print a

print '===== 03'
first_key = [1, 2, 3]
second_key = (1, 2, 3)
my_dict = {}
my_dict[first_key] = 1
my_dict[second_key] = 1
print my_dict
