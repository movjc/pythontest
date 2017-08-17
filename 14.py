#coding=utf-8
"""
date:2017-08-18
@author: ray
将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。
"""
input = int(raw_input("请输入要分解的正整数："))
temp = []
while input!=1:
    for i in range(2,input+1):
        if input%i == 0:
            temp.append(i)
            input = input /i
            break
        
print temp