#coding=utf-8
"""
date:2017-08-19
@author: ray
打印出如下图案（菱形）:
   *
  ***
 *****
*******
 *****
  ***
   *
"""

for i in range(4):
    print((3-i)*' '+(2*i+1)*'*')
for i in range(3):
    print((i+1)*' '+(5-2*i)*'*')