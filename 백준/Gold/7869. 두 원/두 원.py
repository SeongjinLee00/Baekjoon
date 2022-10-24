import math

x1,y1,r1,x2,y2,r2=map(float,input().split())

dd=((x2-x1)**2+(y2-y1)**2)**0.5

if dd>=r1+r2:
    print('0.000')
elif dd<=abs(r1-r2):
    if r1<r2:
        print(f'{math.pi*r1*r1:.3f}')
    else:
        print(f'{math.pi*r2*r2:.3f}')
else:
    theta1=math.acos((-r2*r2+r1*r1+dd*dd)/(2*r1*dd))
    theta2=math.acos((-r1*r1+r2*r2+dd*dd)/(2*r2*dd))

    b1=r1*r1*theta1
    b2=r2*r2*theta2

    c1=0.5*r1*r1*math.sin(2*theta1)
    c2=0.5*r2*r2*math.sin(2*theta2)

    print(f'{b1+b2-c1-c2:.3f}')