# -*- coding: utf-8 -*-
#!/usr/bin/python
import math
def getangle(x,y):
    x1=x[0]
    y1=x[1]
    z1=x[2]
    x3=y[0]
    y3=y[1]
    z3=y[2]
    theta=math.acos(z3/((x3*x3+y3*y3+z3*z3)**0.5+float("1e-10")))
    theta1=round(theta,3)
    if y3 > 0:
        fai=math.acos(x3/((x3*x3+y3*y3)**0.5+float("1e-10")))
    else:
        fai=-math.acos(x3/((x3*x3+y3*y3)**0.5+float("1e-10")))
    fai1=round(fai,3)
        #先绕z轴旋转fai角，再绕y轴旋转theta角
    x4=math.cos(theta)*math.cos(fai)*x1-math.cos(theta)*math.sin(fai)*y1+math.sin(theta)*z1
    y4=math.sin(fai)*x1+math.cos(fai)*y1
    z4=-math.sin(theta)*math.cos(fai)*x1+math.sin(theta)*math.sin(fai)*y1+math.cos(theta)*z1
    if y4 > 0:
        beta=math.acos(x4/((x4*x4+y4*y4)**0.5+float("1e-10")))
    else:
        beta=-math.acos(x4/((x4*x4+y4*y4)**0.5+float("1e-10")))
    beta1=round(beta,3)
    result=[fai1,theta1,beta1]       #角度制  
    return result
