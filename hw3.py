import string as s
import math as m

def hw1():
    filename=str(input('파일 이름을 입력하세요: '))
    infile=open(filename,"r")
    lines=infile.read()
    S=list(s.ascii_lowercase)
    B=list(s.ascii_uppercase)
    alpha_list=S+B
    a={}
    for i in range(52):
        x=0
        x=lines.count(alpha_list[i])
        a[alpha_list[i]]=x
        if x==0:
            del a[alpha_list[i]]
    
    print(a)


def hw2():
    file=open("C:\\numbers.txt", 'r')
    line=file.read()
    a=line.split()
    m=list(map(float, a))
    l=len(m)
    rfile=open("C:\\Users\yoonc\Desktop\output.txt",'w')
    data="합계: %f \n 평균: %f" %(sum(m),(sum(m)/l))
    rfile.write(data)




class Circle:
    radius=100
    def clacPerimeter(self,radius):
        return 2*radius*m.pi
    
    def claArea(self,radius):
        return radius*radius*m.pi
    

def hw3():
    c=Circle()
    r=100
    print("반지름: %f 원의 면적: %f 원의 둘레: %f" %(r,c.claArea(r),c.clacPerimeter(r)))


import turtle

class Myturtle(turtle.Turtle):
    def drawSquare(self):
        for i in range(4):
            self.right(90)
            self.forward(100)

def hw4():
    my_turtle=Myturtle()
    my_turtle.forward(100)
    my_turtle.drawSquare()
    
    

     
hw4()
