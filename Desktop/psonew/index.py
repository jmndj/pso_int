#!/usr/bin/python
# -*- coding: utf-8 -*-
def index(x):
    va=abs(x[0])
    vb=abs(x[1])
    vc=abs(x[2])
    t=va
    if t < vb:
        t=vb
    if t < vc:
        t=vc
    y=(round(x[0]/t*10),round(x[1]/t*10),round(x[2]/t*10))   #将晶面法向方向整数化
    return y

            
      










