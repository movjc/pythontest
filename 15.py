#coding=utf-8
"""
date:2017-08-18
@author: ray
题目：利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。
程序分析：程序分析：(a>b)?a:b这是条件运算符的基本例子。
"""
a = int(raw_input('请输入分数:'))
#1
#print 'A' if a>89 else('B' if a>59 else 'C')

ar = [90,60,0]
res = ['A','B','C']
for i in range(0,3):
    if a>ar[i]:
        print res[i]
        break

