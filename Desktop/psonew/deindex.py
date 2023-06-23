#!/usr/bin/python
# -*- coding: utf-8 -*-
from gcd import gcd
import math
def sign(x):
    if x < 0:
        return 0
    else:
        return 1
def calculate(x,y):
    if sign(x) == sign(y):
        return 1
    else:
        return 0
def dezero(x,y,z):
    line=[x,y,z]
    num=0
    for i in range(0,3):
        if line[i] == 0:
            num+=1
    return num
def deindex(x):
    a=x[0]
    b=x[1]
    c=x[2]
    num=dezero(a,b,c)
    if num == 0:
        vec1=[0,-int(c),int(b)]
        vec2=[-int(c),0,int(a)]
        vec3=[-int(b),int(a),0]
        vec4=[0,0,0]
        vec5=[0,0,0]
        vec6=[0,0,0]
        base1=list(gcd(vec1))
        base2=list(gcd(vec2))
        base3=list(gcd(vec3))
        if calculate(base1[2],base2[2]) == 1:
            for i in range(0,3):
                vec4[i]=base1[i]-base2[i]
        else:
            for i in range(0,3):
                vec4[i]=base1[i]+base2[i]
        if calculate(base1[1],base3[1]) == 1:
            for i in range(0,3):
                vec5[i]=base1[i]-base3[i]
        else:
            for i in range(0,3):
                vec5[i]=base1[i]+base3[i]
        if calculate(base2[0],base3[0]) == 1:
            for i in range(0,3):
                vec6[i]=base2[i]-base3[i]
        else:
            for i in range(0,3):
                vec6[i]=base2[i]+base3[i]
        v4=[int(vec4[0]),int(vec4[1]),int(vec4[2])]
        v5=[int(vec5[0]),int(vec5[1]),int(vec5[2])]
        v6=[int(vec6[0]),int(vec6[1]),int(vec6[2])]
        base4=list(gcd(v4))
        base5=list(gcd(v5))
        base6=list(gcd(v6))
        return [base1,base2,base3,base4,base5,base6]
    if num == 1:
        if a==0:
            base1=[1,0,0]
            base2=[-1,0,0]
            vec3=[0,-int(c),int(b)]
            vec4=[0,int(c),-int(b)]
            base3=list(gcd(vec3))
            base4=list(gcd(vec4))
        if b==0:
            base1=[0,1,0]
            base2=[0,-1,0]
            vec3=[-int(c),0,int(a)]
            vec4=[int(c),0,-int(a)]
            base3=list(gcd(vec3))
            base4=list(gcd(vec4))
        if c==0:
            base1=[0,0,1]
            base2=[0,0,-1]
            vec3=[-int(b),int(a),0]
            vec4=[int(b),-int(a),0]
            base3=list(gcd(vec3))
            base4=list(gcd(vec4))
        return [base1,base2,base3,base4]
    if num == 2:
        if a ==0 and b ==0:
            base1=[1,0,0]
            base2=[0,1,0]
            base3=[1,1,0]
        if a ==0 and c ==0:
            base1=[1,0,0]
            base2=[0,0,1]
            base3=[1,0,1]
        if b ==0 and c ==0:
            base1=[0,1,0]
            base2=[0,0,1]
            base3=[0,1,1]
        return [base1,base2,base3]
            


            
      










