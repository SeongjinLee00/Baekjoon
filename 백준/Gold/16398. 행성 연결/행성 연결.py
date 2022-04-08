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

arr=[]

for _ in range(N):
    arr.append(list(map(int,input().split())))

graph=[]
for i in range(N):
    for j in range(N):
        graph.append([i+1,j+1,arr[i][j]])

parent=[i for i in range(N+1)]

graph.sort(key=lambda x:x[2])

ans=0
for start,end,cost in graph:

    if find(start)!=find(end):
        ans+=cost
        union(start,end)

print(ans)