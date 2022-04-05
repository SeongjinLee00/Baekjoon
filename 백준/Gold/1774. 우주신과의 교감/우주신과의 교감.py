def union(x,y):
    a=find(x)
    b=find(y)

    parent[max(a,b)]=min(a,b)

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])

    return parent[x]

N,M=map(int,input().split())

stars=[0]

parent=[i for i in range(N+1)]

graph=[]

for _ in range(N):
    x,y=map(float,input().split())
    stars.append([x,y])

for _ in range(M):
    a,b=map(int,input().split())

    union(a,b)

for i in range(1,len(stars)-1):
    for j in range(i,len(stars)):
        distance=((stars[i][0]-stars[j][0])**2+(stars[i][1]-stars[j][1])**2)**0.5

        graph.append([i,j,distance])

graph.sort(key=lambda x:x[2])

ans=0
for start,end,cost in graph:
    if find(start)!=find(end):
        union(start,end)
        ans+=cost

print(f'{ans:.2f}')