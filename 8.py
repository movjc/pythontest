#coding=utf-8
"""
date:2017-08-17
@author: ray
输出 9*9 乘法口诀表
"""
for i in range(1,10):
    print 
    for j in range(1,i+1):
        #print "%d*%d=%d" %(i,j,i*j),
        print "{}*{}={}".format(j,i,j*i),