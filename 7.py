#coding=utf-8
"""
date:2017-08-17
@author: ray
将一个列表的数据复制到另一个列表中
"""
import copy
a = [1,2,3,4]
b = a[:]
print b

c = copy.copy(a)
print c 

p = []
for i in range(len(a)):
    p.append(a[i])
print p