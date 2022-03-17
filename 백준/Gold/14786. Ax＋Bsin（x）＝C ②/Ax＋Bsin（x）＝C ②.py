import math

A,B,C=map(int,input().split())

x=50000
dx=50000/2
iter=999999
i=0
while i<iter:
    value=A*x+B*math.sin(x)

    if value>C:
        x=x-dx
        dx=dx/2
    elif value<C:
        x=x+dx
        dx=dx/2
    
    i+=1

print(x)