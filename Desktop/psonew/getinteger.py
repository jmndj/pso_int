# -*- coding: utf-8 -*-
#!/usr/bin/python
import math
from gcd import gcd
from index import index
def getinteger(x):
    N1=(-math.cos(x[0])*math.sin(x[1]),math.sin(x[0])*math.sin(x[1]),math.cos(x[1]))
    intN1=index(N1)
    qa=math.cos(x[0])*math.cos(x[1])*math.cos(x[2])-math.sin(x[0])*math.sin(x[2])
    qb=-math.sin(x[0])*math.cos(x[1])*math.cos(x[2])-math.cos(x[0])*math.sin(x[2])
    qc=math.sin(x[1])*math.cos(x[2]) 
    x1=N1[0]
    x2=N1[1]
    x3=N1[2]
    y1=qa
    y2=qb
    y3=qc
    z1=x2*y3-y2*x3
    z2=x3*y1-x1*y3
    z3=x1*y2-x2*y1   #求出晶面法向向量和剪切方向向量的叉乘
    fa=(z1,z2,z3)
    intfa=index(fa)  #将叉乘的结果整数化
    x1=intfa[0]
    x2=intfa[1]
    x3=intfa[2]
    y1=intN1[0]
    y2=intN1[1]
    y3=intN1[2]

    z1=x2*y3-y2*x3
    z2=x3*y1-x1*y3
    z3=x1*y2-x2*y1   #根据整数化后的晶面法向向量和叉乘向量进行叉乘得到新的剪切方向
    z=[z1,z2,z3]
    result=(intN1,z)
    return result
    






