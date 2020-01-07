#Runge-Kutta 2nd order

from numpy import *

# differential equation
def f(x,y):
    return (2*sin(3*x)-( (x**2)*(y**2) ))/exp(y)
################################################
# RK2
def rk2(x0,xn,xi,yi,h,a2):
    steps=int(((xn-x0)/h)+1)
    xr=zeros(steps)
    yr=zeros(steps)
    a1=1-a2
    p=.5/a2
    q=.5/a2
    xr[0]=xi
    yr[0]=yi
    for k in range(steps-1):
        k1=f(xr[k],yr[k])
        k2=f(xr[k]+p*h, yr[k]+q*k1*h)
        yr[k+1]=yr[k]+(a1*k1+a2*k2)*h
        xr[k+1]=xr[k]+h
    return xr,yr
# Print Function
def rkprint(a2):
    x1,x2,x3,x4=[],[],[],[]
    y1,y2,y3,y4=[],[],[],[]

    x1,y1=rk2(x0,xn,xi,yi,stepsize[0],a2)
    x2,y2=rk2(x0,xn,xi,yi,stepsize[1],a2)
    x3,y3=rk2(x0,xn,xi,yi,stepsize[2],a2)
    x4,y4=rk2(x0,xn,xi,yi,stepsize[3],a2)

    figure(1)
    print("a2: ", a2)
    plot(x1,y1, label='h='+str(stepsize[0]))
    plot(x2,y2, label='h='+str(stepsize[1]))
    plot(x3,y3, label='h='+str(stepsize[2]))
    plot(x4,y4, label='h='+str(stepsize[3]))
    legend(loc=3)
    show()
################################################
# bounds
x0=0
xn=1
# initials
xi=0
yi=5

# h values
stepsize=array([0.1, 0.05, 0.025, 0.0125])
# a2 values
a2array=array([1,1/2,2/3])
# function call
rkprint(a2array[0])
rkprint(a2array[1])
rkprint(a2array[2])
