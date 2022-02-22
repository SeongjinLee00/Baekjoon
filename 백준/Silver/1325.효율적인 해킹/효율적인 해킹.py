from collections import deque
import sys

N,M=map(int,input().split())

graph=[[] for _ in range(N+1)]

for _ in range(M):
    a,b=map(int,sys.stdin.readline().split())

    graph[b].append(a)


def bfs(v):
    q=deque([v])
    visited=[0 for _ in range(N+1)]
    visited[v]=1
    cnt=1
    while q:
        v=q.popleft()
        for w in graph[v]:
            if visited[w]==0:
                visited[w]=1
                q.append(w)
                cnt+=1
    return cnt

result=[]
maxcnt=0
for i in range(1,N+1):
    tmp=bfs(i)
    if maxcnt==tmp:
        result.append(i)
    if tmp>maxcnt:
        maxcnt=tmp
        result=[]
        result.append(i)

print(*result)