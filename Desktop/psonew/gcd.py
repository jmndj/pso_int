#!/usr/bin/python
# -*- coding: utf-8 -*-
import math
def gcd(x):     #gcd为python求最大公约数的函数
    a=abs(x[0])
    b=abs(x[1])
    c=abs(x[2])
    if a != 0 and b != 0 and c != 0:
        p=math.gcd(a,b)
        q=math.gcd(p,c)
        y=(x[0]/q,x[1]/q,x[2]/q)
    if a == 0 and b != 0 and c != 0:
        q=math.gcd(b,c)
        y=(x[0]/q,x[1]/q,x[2]/q)
    if b == 0 and a != 0 and c != 0:
        q=math.gcd(a,c)
        y=(x[0]/q,x[1]/q,x[2]/q)
    if c == 0 and a != 0 and b != 0:
        q=math.gcd(a,b)
        y=(x[0]/q,x[1]/q,x[2]/q)
    if a == 0 and b == 0 and c != 0:
        q=c
        y=(x[0]/q,x[1]/q,x[2]/q)
    if b == 0 and c == 0 and a != 0:
        q=a
        y=(x[0]/q,x[1]/q,x[2]/q)
    if a == 0 and c == 0 and b != 0:
        q=b
        y=(x[0]/q,x[1]/q,x[2]/q)
    if a == 0 and b == 0 and c == 0:
        y=(x[0],x[1],x[2])
    return y 

       
