from collections import deque
import sys

N,M,K,X=map(int,input().split())

graph=[[] for _ in range(N+1)]

for _ in range(M):
    a,b=map(int,sys.stdin.readline().split())
    graph[a].append(b)


visited=[0 for _ in range(N+1)]
ans=[]

def bfs():
    q=deque([[X,0]])
    visited[X]=1
    while q:
        v,d=q.popleft()
        if d==K:
            ans.append(v)
        for w in graph[v]:
            if not visited[w]:
                q.append([w,d+1])
                visited[w]=1

bfs()
ans.sort()

for a in ans:
    print(a)
if ans==[]:
    print(-1)