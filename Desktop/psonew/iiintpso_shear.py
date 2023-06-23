#------------------------------------------------------------------------------+

#
#   Nathan A. Rooy
#   Simple Particle Swarm Optimization (PSO) with Python
#   July, 2016
#
#------------------------------------------------------------------------------+

#--- IMPORT DEPENDENCIES ------------------------------------------------------+
# -*- coding: utf-8 -*-
#!/usr/bin/python
from __future__ import division
import random
import math
import os
import sys
import csv
import pandas as pd
import Crystallographic as CC
import theory
import xml.etree.ElementTree
import time
from gcd import gcd 
from index import index 
from deindex import deindex
from getinteger import getinteger
from getangle import getangle
def getmax(x):
    a=abs(x[0])         
    b=abs(x[1])
    c=abs(x[2])
    max = a
    if max<b:
        max = b
    if max<c:
        c = max
    return max
def func1(x):
     if (os.path.exists('tmp.dat')):     
         out = open('tmp.csv','w',newline='')
         csv_writer = csv.writer(out,dialect='excel')
         f = open("tmp.dat","r",encoding='utf-8')    
         for line in f.readlines():
             mylist = line.split()
             csv_writer.writerow(mylist)                        #转化为csv文件
         f.close()
         out.close()
         os.system('rm tmp.dat')
         df = pd.read_csv('./tmp.csv', names=['shear', 'stress'])
         total= df['stress'].max()                            #找出最大值 
         result=-total
     else:
         result=0
     return result
  
#--- MAIN ---------------------------------------------------------------------+

class Particle:                     # 定义一个类
    def __init__(self,x0):
        self.position_i=[]          # particle position
        self.velocity_i=[]          # particle velocity
        self.pos_best_i=[]          # best position individual
        self.normal_best_i=[]
        self.shear_best_i=[]
        self.err_best_i=-1          # best error individual
        self.err_i=0               # error individual
        self.intnormal_i=[0,0,0]     #整数型法向向量 
        self.intshear_i=[0,0,0]      #整数型剪切方向向量
        self.deierr_i=0
        self.angle_i=[0,0,0]
        for i in range(0,num_dimensions):
            self.velocity_i.append(random.uniform(-0.8,0.8))     #random.uniform随机生成一个浮点数，
            self.position_i.append(x0[i])                    #

    
    def evaluate(self,costFunc):                             #定义评估函数
        self.err_i=costFunc(self.position_i)

        if self.err_i < self.err_best_i or self.err_best_i==-1:
            self.pos_best_i=self.position_i
            self.err_best_i=self.err_i
            self.normal_best_i=self.intnormal_i
            self.shear_best_i=self.intshear_i
    def deievaluate(self,costFunc,i,base):
        self.deierr_i=costFunc(self.position_i)

    def update_velocity(self,pos_best_g,i,maxgen):
        wmax=0.9       # constant inertia weight (how much to weigh the previous velocity)
        wmin=0.4
        w=wmin+(wmax-wmin)*(1-i/maxgen)
        cstart1=2.5
        cend1=0.5
        cstart2=0.5
        cend2=3.5
        c1=cstart1+(cend1-cstart1)*(i/maxgen)        # cognative constant
        c2=cstart2+(cend2-cstart2)*(i/maxgen)        # social constant


        for i in range(0,num_dimensions):                     #遍历每个自由度
            r1=random.random()                                #随机生成一个浮点数，范围在[0,1)之间
            r2=random.random()                                

            vel_cognitive=c1*r1*(self.pos_best_i[i]-self.position_i[i])   
            vel_social=c2*r2*(pos_best_g[i]-self.position_i[i])              
            self.velocity_i[i]=w*self.velocity_i[i]+vel_cognitive+vel_social  

    # update the particle position based off new velocity updates
    def update_position(self,bounds):   
        anglenumber=[0,1,2]                      
        for i in anglenumber:                     #遍历每个粒子的自由度
            self.position_i[i]=self.position_i[i]+self.velocity_i[i]   
            if i == 1:
                if self.position_i[i]>bounds[i][1]:
                    self.position_i[i]=bounds[i][1]
                if self.position_i[i]<bounds[i][0]:
                    self.position_i[i]=bounds[i][0]
            else: 
            # adjust maximum position if necessary
                if self.position_i[i]>bounds[i][1]:
                    self.position_i[i]=self.position_i[i]-2*math.pi

            # adjust minimum position if neseccary
                if self.position_i[i] < bounds[i][0]:
                    self.position_i[i]=self.position_i[i]+2*math.pi
    def directory(self,z):   #创建目录
        temp = sys.stdout
        file = open('dir.txt','w')
        sys.stdout = file
        print(z) # 输出旋转粒子标号
        sys.stdout.close()
        os.system('sh dir.sh')       
    def readfile(self,w):
        temp = sys.stdout
        file = open('readfile.txt','w')
        sys.stdout = file
        print(w) # 输出旋转粒子标号
        sys.stdout.close()
        os.system('sh readfile.sh')
    def deireadfile(self,i):
        temp = sys.stdout
        file = open('deireadfile.txt','w')
        sys.stdout = file
        print(i)
        sys.stdout.close()
        os.system('sh deireadfile.sh')
        
#####################################
#获得整数型指数
    def getinteger(self):                            #获得整数型指数
        result=getinteger(self.position_i)
        self.intnormal_i=list(gcd(result[0]))
        self.intshear_i=list(gcd(result[1]))
        self.position_i=getangle(self.intnormal_i,self.intshear_i)       #角度制  
    def getangle(self,i,base):
        self.angle_i=getangle(self.intnormal_i,base[i])
    def intsbatch(self,y):
        X=(1,0,0)
        Y=(0,1,0)
        Z=(0,0,1)
        a=b=c=3.556

        N1=self.intnormal_i
        N2=self.intshear_i
        N3=(CC.Coordinate(N1,N2,a))

        result=theory.matrix(N3,a)
     
        temp = sys.stdout
        file = open('pos','w')
        sys.stdout = file
        print('diamond')
        print(1.0)
        print(result[0][0],result[0][1],result[0][2])
        print(result[1][0],result[1][1],result[1][2])
        print(result[2][0],result[2][1],result[2][2]) # 输出旋转后的基底 
        sys.stdout.close()

        temp = sys.stdout
        file = open('sbatch.txt','w')
        sys.stdout = file
        print(y) # 输出旋转粒子标号
        sys.stdout.close()
        os.system('source ./sbatch.sh')
     
    def deisbatch(self,y,i,base):
        X=(1,0,0)
        Y=(0,1,0)
        Z=(0,0,1)
        a=b=c=3.556

        N1=self.intnormal_i
        N2=base
        N3=(CC.Coordinate(N1,N2,a))

        result=theory.matrix(N3,a)
     
        temp = sys.stdout
        file = open('pos','w')
        sys.stdout = file
        print('diamond')
        print(1.0)
        print(result[0][0],result[0][1],result[0][2])
        print(result[1][0],result[1][1],result[1][2])
        print(result[2][0],result[2][1],result[2][2]) # 输出旋转后的基底 
        sys.stdout.close()

        temp = sys.stdout
        file = open('sbatch.txt','w')
        sys.stdout = file
        print(y) # 输出旋转粒子标号
        sys.stdout.close()

        temp = sys.stdout
        file = open('deisbatch.txt','w')
        sys.stdout = file
        print(i)
        sys.stdout.close()

        os.system('source ./deisbatch.sh')     

        
class PSO():                                                  #定义一个类
    def __init__(self,costFunc,x0,bounds,num_particles,maxiter):
        global num_dimensions                                #   

        num_dimensions=len(x0)                            
        err_best_g=0                   # best error for group
        pos_best_g=[]                   # best position for group
        normal_best_g=[]
        shear_best_g=[]
        swarm=[]                                              #构建粒子群
        for i in range(0,num_particles):                      #遍历所有的粒子               
            swarm.append(Particle(x0))
        for i in range(0,num_particles):
            swarm[i].position_i=[random.uniform(-math.pi,math.pi),random.uniform(0,math.pi),random.uniform(-math.pi,math.pi)]         
        for i in range(0,num_particles):
            swarm[i].directory(i)
        # begin optimization loop
        i=0
        while i < maxiter:
            for j in range(0,num_particles):
                temp = sys.stdout
                file = open('iter.txt','w')
                sys.stdout = file
                print(i) # 输出旋转粒子标号
                sys.stdout.close()
            #    os.system('sh num.sh')
                swarm[j].getinteger()
                swarm[j].intsbatch(j)
            flag=1
            while flag:                                              
                if (os.path.exists('watch.txt')):                    #通过watch.txt文件是否存在判断是否有粒子计算完毕
                    filename="watch.txt"
                    myfile=open(filename)
                    count=len(myfile.readlines())
                    if count == num_particles:                         #
                        flag=0                                        #结束本次while循环                  
                        os.system('rm watch.txt')                     #本代全体粒子迭代结束                                
                time.sleep(10)
            maxsingal=0
            total=0
            errw=0
            for j in range(0,num_particles):                     #遍历每个粒子
                swarm[j].readfile(j)
                swarm[j].evaluate(costFunc)

                err_real_i=-swarm[j].err_i
                if swarm[j].err_i < errw:
                    maxsingal=j
                    errw=swarm[j].err_i
                total=total+err_real_i                  
                if swarm[j].err_i < err_best_g or err_best_g == 0:
                    pos_best_g=list(swarm[j].position_i)
                    err_best_g=float(swarm[j].err_i)
                    normal_best_g=list(swarm[j].intnormal_i)
                    shear_best_g=list(swarm[j].intshear_i)
            vec=list(swarm[maxsingal].intnormal_i)
            base=deindex(vec)
            baselength=len(base)
            for l in range(0,baselength):
                swarm[maxsingal].deisbatch(maxsingal,l,base[l])
                temp = sys.stdout
                file = open('deindex.txt','a+')
                sys.stdout = file
                print(i,maxsingal,l,swarm[maxsingal].intnormal_i,base[l])
                sys.stdout.close()
            flag=1
            while flag:
                if (os.path.exists('watch.txt')):                    #通过watch.txt文件是否存在判断是否有粒子计算完毕
                    filename="watch.txt"
                    myfile=open(filename)
                    count=len(myfile.readlines())
                    if count == baselength:                         #
                        flag=0                                        #结束本次while循环                  
                        os.system('rm watch.txt')                     #本代全体粒子迭代结束                                
                time.sleep(10)
            for k in range(0,baselength):
                swarm[maxsingal].deireadfile(k)
                swarm[maxsingal].deievaluate(costFunc,k,base)
                if swarm[maxsingal].deierr_i < err_best_g:
                    swarm[maxsingal].getangle(k,base)
                    pos_best_g=list(swarm[maxsingal].angle_i)
                    err_best_g=swarm[maxsingal].deierr_i
                    shear_best_g=base[k]
                    normal_best_g=swarm[maxsingal].intnormal_i
                    swarm[maxsingal].pos_best_i=list(swarm[maxsingal].angle_i)
                    swarm[maxsingal].position_i=list(swarm[maxsingal].angle_i)
                if swarm[maxsingal].deierr_i < swarm[maxsingal].err_i:
                    swarm[maxsingal].err_i=swarm[maxsingal].deierr_i
                    swarm[maxsingal].position_i=list(swarm[maxsingal].angle_i)
                    swarm[maxsingal].intshear_i=base[k]
                    if swarm[maxsingal].err_i < swarm[maxsingal].err_best_i:
                        swarm[maxsingal].pos_best_i=swarm[maxsingal].position_i
                        swarm[maxsingal].normal_best_i=swarm[maxsingal].intnormal_i
                        swarm[maxsingal].shear_best_i=swarm[maxsingal].intshear_i
                        swarm[maxsingal].err_best_i=swarm[maxsingal].err_i
                     
            average=total/(num_particles)

            temp = sys.stdout
            file = open('average.txt','a+')
            sys.stdout = file
            print(i,average) # 输出群体最优方向和最优值
            sys.stdout.close()

            err_best_real_g=-err_best_g

            temp = sys.stdout
            file = open('group_best.txt','a+')
            sys.stdout = file
            print(i,normal_best_g,shear_best_g,err_best_real_g) # 输出群体最优方向和最优值
            sys.stdout.close()
            #将每次迭代的结果输出到指定文件里面

            for j in range(0,num_particles):                     #遍历每个粒子
                err_real_i=-swarm[j].err_best_i

                temp = sys.stdout
                file = open('{0}_best.txt'.format(j),'a+')
                sys.stdout = file
                print(i,swarm[j].normal_best_i,swarm[j].shear_best_i) # 输出个体最优方向和最优值
                sys.stdout.close()

                err_real_i=-swarm[j].err_i

                temp = sys.stdout
                file = open('{0}.txt'.format(j),'a+')
                sys.stdout = file
                print(i,swarm[j].intnormal_i,swarm[j].intshear_i,err_real_i) # 输出个体最优方向和最优值
                sys.stdout.close()

                temp = sys.stdout
                file = open('{0}_angle.txt'.format(j),'a+')
                sys.stdout = file
                print(i,swarm[j].position_i,err_real_i)
                sys.stdout.close()
            
            for j in range(0,num_particles):
                swarm[j].update_velocity(pos_best_g,i,maxiter)
                swarm[j].update_position(bounds)
            i+=1

        # print final results
        err_best_g_real=-err_best_g
        temp = sys.stdout
        file = open('psoresult','w')
        sys.stdout = file
        print('FINAL:')
        print(pos_best_g)
        print(err_best_g_real)
        sys.stdout.close()        

if __name__ == "__PSO__":
    main()

#--- RUN ----------------------------------------------------------------------+
initial=[1,1,1]               # initial starting location [x1,x2...]
bounds=[(-math.pi,math.pi),(0,math.pi),(-math.pi,math.pi)]  # input bounds [(x1_min,x1_max),(x2_min,x2_max)...]
PSO(func1,initial,bounds,num_particles=15,maxiter=30)

#--- END ----------------------------------------------------------------------+
