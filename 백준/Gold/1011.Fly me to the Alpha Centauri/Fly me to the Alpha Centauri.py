import math

T=int(input())
for _ in range(T):
    x,y=map(int,input().split())
    distance=y-x

    n=int(math.sqrt(distance))
    

    if distance==n*n:
        print(2*n-1)
    elif n*n+1<=distance<=n*n+n:
        print(2*n)
    elif distance>=n*n+n+1:
        print(2*n+1)