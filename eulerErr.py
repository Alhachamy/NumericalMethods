from numpy import *

def f(x,y):
    return -2.2067*(10**-12)*( (y**4) - (81*(10**8)) )

def euler(h,x0,xn,xi,yi):
    xs=linspace(x0,xn,int((xn-x0)/h)+1)
    x=zeros(len(xs))
    y=zeros(len(xs))
    x[0]=xi
    y[0]=yi
    for i in range(len(xs)-1):
        y[i+1]=y[i]+f(x[i], y[i])*h
        x[i+1]=x[i]+h
    return x,y

def eulerError(h,x0,xn,xi,yi,actual):
    xs=linspace(x0,xn,int((xn-x0)/h)+1)
    for j in range(0,len(xs)-1):
        approx=yi+f(xi,yi)*h
        xi=xi+h
        yi=approx
        
    print("Step: ",h,"Approx: ", yi,"True Error: ",actual-yi, "Error %: ",abs((actual-yi)/actual)*100 )
    return yi
    
################################################
x0=0
xn=480

xi=0
yi=1200
actual=647.57
stepsize=array([32,16,8,4])

x1=zeros(50)
y1=zeros(50)
x2=zeros(50)
y2=zeros(50)
x3=zeros(50)
y3=zeros(50)
x4=zeros(50)
y4=zeros(50)

x1,y1 = euler(stepsize[0],x0,xn,xi,yi)
x2,y2 = euler(stepsize[1],x0,xn,xi,yi)
x3,y3 = euler(stepsize[2],x0,xn,xi,yi)
x4,y4 = euler(stepsize[3],x0,xn,xi,yi)

stepDepY=zeros(4)
for i in range(len(stepsize)):
    stepDepY[i]=eulerError(stepsize[i],x0,xn,xi,yi,actual)
    

    
figure(1)
plot(x1,y1,label='h='+str(stepsize[0]))
plot(x2,y2,label='h='+str(stepsize[1]))
plot(x3,y3,label='h='+str(stepsize[2]))
plot(x4,y4,label='h='+str(stepsize[3]))
legend(loc=3)
title("Euler\'s method Graph 1")
xlabel("Time")
ylabel("Temp")
show()