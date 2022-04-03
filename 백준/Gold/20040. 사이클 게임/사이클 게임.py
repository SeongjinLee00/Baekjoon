import sys
sys.setrecursionlimit(200000)

n,m=map(int,input().split())

parent=[i for i in range(n)]

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x,y):
    a=find(x)
    b=find(y)

    parent[max(a,b)]=min(a,b)


for turn in range(1,m+1):
    a,b=map(int,sys.stdin.readline().split())

    if find(a)==find(b):
        print(turn)
        exit(0)
    else:
        union(a,b)

print(0)