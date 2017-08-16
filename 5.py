#coding=utf-8
"""
date:2017-08-17
@author: ray
输入三个整数x,y,z，请把这三个数由小到大输出。
"""
l = []
for i in range(3):
    x = int(raw_input("请输入整数:"))
    l.append(x)
    
l.sort()
for j in range(len(l)):
    print l[j],
