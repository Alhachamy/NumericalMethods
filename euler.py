from numpy import *

# differential equation
def f(x,y):
    return (2*sin(3*x)-( (x**2)*(y**2) ))/exp(y)

# Ruler's method
def euler(h,x0,xn,xi,yi):
    xs=linspace(x0,xn,int((xn-x0)/h)+1)
    x=zeros(len(xs))
    y=zeros(len(xs))
    x[0]=xi
    y[0]=yi
    for i in range(0,len(xs)-1):
        y[i+1]=y[i]+f(x[i], y[i])*h
        x[i+1]=x[i]+h
    return x,y
################################################
#bounds
x0=0
xn=1
# initials
xi=0
yi=5

# stepsize
stepsize=array([0.1, 0.05, 0.025, 0.0125])
# arrays to store output for each step size
x1=zeros(50)
y1=zeros(50)
x2=zeros(500)
y2=zeros(500)
x3=zeros(500)
y3=zeros(500)
x4=zeros(500)
y4=zeros(500)

# function calls
x1,y1 = euler(stepsize[0],x0,xn,xi,yi)
x2,y2 = euler(stepsize[1],x0,xn,xi,yi)
x3,y3 = euler(stepsize[2],x0,xn,xi,yi)
x4,y4 = euler(stepsize[3],x0,xn,xi,yi)


# plots
figure(1)
plot(x1,y1,label='h='+str(stepsize[0]))
plot(x2,y2,label='h='+str(stepsize[1]))
plot(x3,y3,label='h='+str(stepsize[2]))
plot(x4,y4,label='h='+str(stepsize[3]))
legend(loc=3)
title("Euler\'s method")
xlabel("x")
ylabel("y")
show()