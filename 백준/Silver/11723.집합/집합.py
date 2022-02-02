import sys

T=int(input())

S=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

for _ in range(T):
    c=sys.stdin.readline().strip()

    if c=='all':
        S=[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    elif c=='empty':
        S=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    else:
        c,n=c.split()
        n=int(n)
        if c=='add':
            S[n-1]=1
        elif c=='check':
            if S[n-1]==1:
                print(1)
            else:
                print(0)
        elif c=='remove':
            S[n-1]=0
        elif c=='toggle':
            if S[n-1]==1:
                S[n-1]=0
            else:
                S[n-1]=1