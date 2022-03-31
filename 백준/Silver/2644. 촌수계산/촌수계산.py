from collections import deque

n=int(input())
s,e=map(int,input().split())
m=int(input())

graph=[[] for _ in range(n+1)]

for _ in range(m):
    u,v=map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

def bfs(start):

    q=deque([[start,0]])
    visited=[0]*(n+1)
    visited[start]=1

    while q:
        v,d=q.popleft()
        if v==e:
            return d
        for w in graph[v]:
            if not visited[w]:
                visited[w]=1
                q.append([w,d+1])

    return -1

print(bfs(s))