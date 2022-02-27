from collections import deque

N=int(input())

graph=[]

for _ in range(N):
    graph.append(list(map(int,input().split())))

ans=[[0]*N for _ in range(N)]

def bfs(start):
    q=deque([start])
    visited=[0 for _ in range(N)]

    while q:
        v=q.popleft()
        for w in range(N):
            if graph[v][w] and not visited[w]:
                q.append(w)
                visited[w]=1
                ans[start][w]=1

for i in range(N):
    bfs(i)

for i in range(N):
    print(*ans[i])