#coding=utf-8
"""
date:2017-08-18
@author: ray
题目：求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。
例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。
"""

Tn = 0
Sn = []
n = int(raw_input('n='))
a = int(raw_input('a='))

for count in range(n):
    Tn = Tn + a
    a = a*10
    Sn.append(Tn)
    print Tn
    
Sn = reduce(lambda x,y:x+y,Sn)
print '计算的和为:',Sn
print a