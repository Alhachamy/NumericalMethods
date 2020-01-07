#RK 4th order
from numpy import *

#differential equation
def f(x,y):
    return exp((-x**2)/2)/sqrt(2*pi)

# Rk4 function
def rk4(x0,xn,xi,yi,h,a2,actual):
    steps=int(((xn-x0)/h)+1)
    x4=zeros(steps)
    y4=zeros(steps)
    a1=1-a2
    p=.5/a2
    q=.5/a2
    x4[0]=xi
    y4[0]=yi
    for n in range(steps-1):
        k1=f(x4[n],y4[n])
        k2=f(x4[n]+.5*h, y4[n]+.5*k1*h)
        k3=f(x4[n]+.5*h, y4[n]+.5*k1*h)
        k4=f(x4[n]+h,y4[n]+h*k3)
        y4[n+1]=y4[n]+1./6*(k1+2*k2+2*k3+k4)*h
        x4[n+1]=x4[n]+h
    return x4,y4
    
    
################################################
# intervals
x0=0
xn=1
# initials
xi=0
yi=0
# actual solution
actual=0.34134474606855
# h value
stepsize=array([1,0.5,0.05,0.025])
# a2 value, best to use 1, 1/2, 2/3
a2=2/3

x1,y1=rk4(x0,xn,xi,yi,stepsize[0],a2,actual)
x2,y2=rk4(x0,xn,xi,yi,stepsize[1],a2,actual)
x3,y3=rk4(x0,xn,xi,yi,stepsize[2],a2,actual)
x4,y4=rk4(x0,xn,xi,yi,stepsize[3],a2,actual)

figure(1)
title("RK4")
plot(x1,y1, label='h='+str(stepsize[0]))
plot(x2,y2, label='h='+str(stepsize[1]))
plot(x3,y3, label='h='+str(stepsize[2]))
plot(x4,y4, label='h='+str(stepsize[3]))
legend(loc=2)
show()