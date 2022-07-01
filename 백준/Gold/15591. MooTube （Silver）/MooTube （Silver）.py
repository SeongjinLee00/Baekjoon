from collections import deque

N,Q=map(int,input().split())

graph=[[] for _ in range(N)]

for _ in range(N-1):
    s,e,u=map(int,input().split())

    graph[s-1].append([u,e-1])
    graph[e-1].append([u,s-1])

for _ in range(Q):
    u,s=map(int,input().split())
    q=deque([s-1])
    visited=[0]*N
    visited[s-1]=1
    cnt=0

    while q:
        now=q.popleft()
        for usado, next in graph[now]:
            if not visited[next] and usado>=u:
                q.append(next)
                visited[next]=1
                cnt+=1

    print(cnt)