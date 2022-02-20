import sys
from collections import deque

N=int(sys.stdin.readline())
M=int(sys.stdin.readline())

relations=[[0]*(N+1) for _ in range(N+1)]
for _ in range(M):
    a,b=map(int,sys.stdin.readline().split())
    relations[a][b]=1
    relations[b][a]=1

q=deque([1])
visited=[]
def bfs():
    visited.append(1)

    while q:
        v=q.popleft()
        for w in range(N+1):
            if relations[v][w]==1 and w not in visited:
                q.append(w)
                visited.append(w)
bfs()
print(len(visited)-1)