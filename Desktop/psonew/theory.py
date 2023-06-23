#!/usr/bin/python
# -*- coding: utf-8 -*-

def matrix(N,a):
    b=c=a
    X1=1
    Y1=0
    Z1=0;
    X2=0
    Y2=1
    Z2=0
    X3=0
    Y3=0
    Z3=1
    x1=N[0][0]
    y1=N[0][1]
    z1=N[0][2]
    x2=N[1][0]
    y2=N[1][1]
    z2=N[1][2]
    x3=N[2][0]
    y3=N[2][1]
    z3=N[2][2]
    V=1/(X1*(Y2*Z3-Y3*Z2)-Y1*(X1*Z3-X3*Z2)+Z1*(X2*Y3-X3*Y2)+float("1e-10"));
    a11=V*(x1*(Y2*Z3-Z2*Y3)+y1*(X3*Z2-X2*Z3)+z1*(X2*Y3-X3*Y2));
    a12=V*(x2*(Y2*Z3-Z2*Y3)+y2*(X3*Z2-X2*Z3)+z2*(X2*Y3-X3*Y2));
    a13=V*(x3*(Y2*Z3-Z2*Y3)+y3*(X3*Z2-X2*Z3)+z3*(X2*Y3-X3*Y2));
    a21=V*(x1*(Y3*Z1-Y1*Z3)+y1*(X1*Z3-X3*Z1)+z1*(X3*Y1-X1*Y3));
    a22=V*(x2*(Y3*Z1-Y1*Z3)+y2*(X1*Z3-X3*Z1)+z2*(X3*Y1-X1*Y3));
    a23=V*(x3*(Y3*Z1-Y1*Z3)+y3*(X1*Z3-X3*Z1)+z3*(X3*Y1-X1*Y3));
    a31=V*(x1*(Y1*Z2-Y2*Z1)+y1*(X2*Z1-X1*Z2)+z1*(X1*Y2-Y1*X2));
    a32=V*(x2*(Y1*Z2-Y2*Z1)+y2*(X2*Z1-X1*Z2)+z2*(X1*Y2-Y1*X2));
    a33=V*(x3*(Y1*Z2-Y2*Z1)+y3*(X2*Z1-X1*Z2)+z3*(X1*Y2-Y1*X2));


    B=1/(a11*(a22*a33-a23*a32)-a21*(a12*a33-a13*a32)+a31*(a12*a23-a13*a22)+float("1e-10"));
    b11=B*(a22*a33-a23*a32);
    b12=B*(a13*a32-a12*a33);
    b13=B*(a12*a23-a13*a22);
    b21=B*(a23*a31-a21*a33);
    b22=B*(a11*a33-a13*a31);
    b23=B*(a21*a13-a11*a23);
    b31=B*(a21*a32-a22*a31);
    b32=B*(a12*a31-a11*a32);
    b33=B*(a11*a22-a21*a12);

    a=(b11*a,b21*a,b31*a)
    b=(b12*b,b22*b,b32*b)
    c=(b13*c,b23*c,b33*c)

    return(a,b,c)

#仅在立方坐标系下使用,共有3个参数
def Coordinate(Plane,Crystallographic,a):
    c=b=a
    o1= Plane[0]*a 
    o2= Plane[1]*b
    o3= Plane[2]*c
    o4=(o1*o1+o2*o2+o3*o3)**0.5
    x3=o1/(o4+float("1e-10"))
    y3=o2/(o4+float("1e-10"))
    z3=o3/(o4+float("1e-10"))
    o1= Crystallographic[0]*a
    o2= Crystallographic[1]*b
    o3= Crystallographic[2]*c
    o4=(o1*o1+o2*o2+o3*o3)**0.5
    x1=o1/(o4+float("1e-10"))
    y1=o2/(o4+float("1e-10"))
    z1=o3/(o4+float("1e-10"))
    

    o1=y1*z3-y3*z1
    o2=-(x1*z3-x3*z1)
    o3=x1*y3-x3*y1
    o4=(o1*o1+o2*o2+o3*o3)**0.5
    x2=-o1/(o4+float("1e-10"))
    y2=-o2/(o4+float("1e-10"))
    z2=-o3/(o4+float("1e-10"))
    return(x1,y1,z1),(x2,y2,z2),(x3,y3,z3)
       
