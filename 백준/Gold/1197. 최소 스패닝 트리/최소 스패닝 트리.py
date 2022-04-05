def union(x,y):
    a=find(x)
    b=find(y)

    parent[max(a,b)]=min(a,b)

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])

    return parent[x]

V,E=map(int,input().split())
parent=[i for i in range(V+1)]

graph=[]

for _ in range(E):
    u,v,w=map(int,input().split())
    graph.append([u,v,w])

graph.sort(key=lambda x:x[2])

ans=0
for start,end,cost in graph:
    if find(start)!=find(end):
        union(start,end)
        ans+=cost

print(ans)