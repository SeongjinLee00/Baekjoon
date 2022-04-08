import sys

def union(x,y):
    a=find(x)
    b=find(y)

    parent[max(a,b)]=min(a,b)
    
def find(x):

    if x!=parent[x]:
        parent[x]=find(parent[x])

    return parent[x]

N=int(input())
M=int(input())
parent=[i for i in range(N+1)]
graph=[]

for _ in range(M):
    graph.append(list(map(int,sys.stdin.readline().split())))

graph.sort(key=lambda x:x[2])

ans=0
for start,end,cost in graph:
    if find(start)!=find(end):
        ans+=cost
        union(start,end)

print(ans)