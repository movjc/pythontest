#coding=utf-8
"""
date:2017-08-17
@author: ray
斐波那契数列
"""
def fib(n):
    a,b = 1,1
    for i in range(n-1):
        a,b = b,a+b
    return a

def fib1(n):
    if n ==1 or n ==2:
        return 1
    return fib1(n-1) + fib1(n-2)

print fib(10),fib1(10)