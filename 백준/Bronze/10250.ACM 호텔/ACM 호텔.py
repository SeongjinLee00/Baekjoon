from math import ceil

T=int(input())

X=0
Y=0
for _ in range(T):
    H,W,N=map(int,input().split())
    X=ceil(N/H)
    if N%H==0:
        Y=H
    else:
        Y=N%H
    
    if X<10:
        print(f'{Y}'+'0'+f'{X}')
    else:
        print(f'{Y}{X}')