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
gender=[0]+list(input().split())

parent=[i for i in range(N+1)]
graph=[]

for _ in range(M):
    graph.append(list(map(int,sys.stdin.readline().split())))

graph.sort(key=lambda x:x[2])

ans=0
cnt=0
for start,end,cost in graph:
    if gender[start]==gender[end]:
        continue
    if find(start)!=find(end):
        ans+=cost
        cnt+=1
        union(start,end)

if cnt==N-1:
    print(ans)
else:
    print(-1)