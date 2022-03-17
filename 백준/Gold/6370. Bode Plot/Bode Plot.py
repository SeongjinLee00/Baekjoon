import math

Vs,R,C,n=input().split()
Vs=float(Vs)
R=float(R)
C=float(C)
n=int(n)

for _ in range(n):
    w=float(input())

    magnitude=Vs*w*C*R/math.sqrt((w*C*R)**2+1)

    print(f'{magnitude:.3f}')