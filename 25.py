#coding=utf-8
"""
date:2017-08-19
@author: ray
求1+2!+3!+...+20!的和
"""
n = 0
s = 0
t = 1
l = []
for n in range(1,21):
    t *= n
    l.append(t)
    s += t
    
print '1! + 2! + 3! + ... + 20! = %d' % s
print(reduce(lambda x ,y : x + y,l))

s = 1
z = []
for i in range(1,21):
    s *= i
    z.append(s)
print(sum(z)-1)