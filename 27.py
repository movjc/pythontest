#coding=utf-8
"""
date:2017-08-19
@author: ray
用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来
"""
def output(s,L):
    if L == 0:
        return
    print (s[L-1])
    output(s,L-1)
    
s = raw_input('Input a string')
L = len(s)
output(s,L)