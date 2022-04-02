import sys

n,m=map(int,input().split())

parent=[i for i in range(n+1)]

def union(x,y):
    parent[findset(y)]=findset(x)

def findset(x):
    while x!=parent[x]:
        x=parent[x]
    return x

for _ in range(m):
    num,a,b=map(int,sys.stdin.readline().split())

    if num==0:
        union(a,b)
    elif num==1:
        p1=findset(a)
        p2=findset(b)
        if p1==p2:
            print('YES')
        else:
            print('NO')