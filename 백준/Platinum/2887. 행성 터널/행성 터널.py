V=int(input())

parent=[i for i in range(V+1)]

def union(x,y):
    a=find(x)
    b=find(y)

    parent[max(a,b)]=min(a,b)

def find(x):

    if parent[x]!=x:
        parent[x]=find(parent[x])

    return parent[x]

coordinates=[]
idx=1

for _ in range(V):
    x,y,z=map(int,input().split())

    coordinates.append([x,y,z,idx])
    idx+=1

graphs=[]

coordinates.sort(key=lambda x:x[0])

for i in range(len(coordinates)-1):
    graphs.append([coordinates[i][3], coordinates[i+1][3],coordinates[i+1][0]-coordinates[i][0]])

coordinates.sort(key=lambda x:x[1])
for i in range(len(coordinates)-1):
    graphs.append([coordinates[i][3], coordinates[i+1][3],coordinates[i+1][1]-coordinates[i][1]])

coordinates.sort(key=lambda x:x[2])
for i in range(len(coordinates)-1):
    graphs.append([coordinates[i][3], coordinates[i+1][3],coordinates[i+1][2]-coordinates[i][2]])

graphs.sort(key=lambda x:x[2])

ans=0
for s,e,w in graphs:
    if find(s)!=find(e):
        union(s,e)
        ans+=w

print(ans)