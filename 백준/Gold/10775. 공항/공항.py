def union(x,y):
    a=find(x)
    b=find(y)

    parent[max(a,b)]=min(a,b)

def find(x):
    if parent[x]!=x:
        parent[x]=find(parent[x])
    
    return parent[x]

import sys

input=sys.stdin.readline

G=int(input())
P=int(input())
parent=[i for i in range(G+1)]
cnt=0

for _ in range(P):
    airplane=int(input())
    gate=find(airplane)
    if gate==0:
        print(cnt)
        exit(0)
    if gate<=airplane:
        cnt+=1
        union(gate-1,gate)

print(cnt)