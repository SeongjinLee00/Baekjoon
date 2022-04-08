import sys

def union(x,y):
    a=find(x)
    b=find(y)

    parent[max(a,b)]=min(a,b)
    
def find(x):

    if x!=parent[x]:
        parent[x]=find(parent[x])

    return parent[x]

N,M=map(int,input().split())
parent=[i for i in range(N+1)]
graph=[]

for _ in range(M):
    graph.append(list(map(int,sys.stdin.readline().split())))

graph.sort(key=lambda x:x[2])

ans=[]
for start,end,cost in graph:
    if find(start)!=find(end):
        ans.append(cost)
        union(start,end)

print(sum(ans)-ans[-1])