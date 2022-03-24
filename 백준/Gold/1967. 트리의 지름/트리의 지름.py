from collections import deque

import sys
N=int(input())

graph=[[] for _ in range(N+1)]

for _ in range(N-1):
    a,b,c=map(int,sys.stdin.readline().split())

    graph[a].append([b,c])
    graph[b].append([a,c])

def bfs(node):
    visited=[0]*(N+1)
    distances=[0]*(N+1)
    q=deque([[node,0]])
    visited[node]=1

    while q:
        v,d=q.popleft()
        distances[v]=d
        for w, nd in graph[v]:
            if not visited[w]:
                q.append([w,d+nd])
                visited[w]=1

    m=max(distances)

    return m, distances.index(m)

r1,r2=bfs(1)

m,d=bfs(r2)

print(m)