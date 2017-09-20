#coding=utf-8
"""
date:2017-08-17
@author: ray
题目：打印出所有的"水仙花数"，所谓"水仙花数"是指一个三位数，其各位数字立方和等于该数本身。例如：153是一个"水仙花数"，因为153=1的三次方＋5的三次方＋3的三次方。
程序分析：利用for循环控制100-999个数，每个数分解出个位，十位，百位。
"""
"""
for n in range(100,1000):
    i = n/100  #百位上的数
    j = n/10%10 #十位上的数
    k = n%10 #各位上的数
    
    if n == i**3 + j**3 + k**3:
        print n
  
for x in range(1,10):
    for y in range(0,10):
        for z in range(0,10):
            s1 = x*100 + y*10 +z
            s2 = pow(x,3) + pow(y,3) + pow(z,3)
            if s1 == s2:
                print s1
  """    
for i in range(100,1000):
      s = str(i)
      if int(s[0])**3 + int(s[1])**3 + int(s[2])**3 == i:
          print i