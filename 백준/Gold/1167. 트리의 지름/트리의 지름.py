from collections import deque

N=int(input())

graph=[[] for _ in range(N+1)]

for _ in range(N):
    numbers=list(map(int,input().split()))

    for i in range(1,len(numbers)-1,2):
        graph[numbers[0]].append([numbers[i],numbers[i+1]])
        graph[numbers[i]].append([numbers[0],numbers[i+1]])

def bfs(node):
    q=deque([[node,0]])
    visited=[0]*(N+1)
    visited[node]=1
    distances=[0]*(N+1)

    while q:
        v,d=q.popleft()
        distances[v]=d
        for w,nd in graph[v]:
            if not visited[w]:
                q.append([w,d+nd])
                visited[w]=1

    p=max(distances)
    return p,distances.index(p)

r1,r2=bfs(1)

maxd,maxdidx=bfs(r2)

print(maxd)