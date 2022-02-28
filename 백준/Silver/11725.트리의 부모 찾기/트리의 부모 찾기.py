from collections import deque

N=int(input())

tree=[[] for _ in range(N+1)]
parents=[-1 for _ in range(N+1)]

for _ in range(N-1):
    a,b=map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)

visited=[0 for _ in range(N+1)]
def bfs():
    q=deque([1])
    visited[1]=0
    while q:
        v=q.popleft()
        for w in tree[v]:
            if not visited[w]:
                q.append(w)
                visited[w]=1
                parents[w]=v

bfs()

for i in range(2,len(parents)):
    print(parents[i])