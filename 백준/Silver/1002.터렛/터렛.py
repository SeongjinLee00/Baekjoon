import math

T=int(input())

for _ in range(T):
    x1,y1,r1,x2,y2,r2=map(int,input().split())

    d=math.sqrt((x2-x1)**2+(y2-y1)**2)

    if d==0 and r1==r2:
        print(-1)
    elif d==abs(r1-r2): #내접
        print(1)
    elif d==r1+r2: #외접
        print(1)
    elif abs(r1-r2)<d<(r1+r2): #두점에서만나
        print(2)
    else:
        print(0)