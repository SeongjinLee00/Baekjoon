import sys
from collections import deque,defaultdict
input = sys.stdin.readline

N,M=map(int,input().split())

lights=[[0]*N for _ in range(N)]

lights[0][0]=1

switches=defaultdict(list)

for _ in range(M):
    a,b,c,d=map(int,input().split())

    switches[(a-1,b-1)].append((c-1,d-1))

dr=[1,-1,0,0]
dc=[0,0,1,-1]
def bfs(r,c):
    visited=[[0]*N for _ in range(N)]
    q=deque([[0,0]])
    visited[0][0]=1

    while q:
        r,c=q.popleft()
        if (r,c) in switches:
            for a,b in switches[(r,c)]:
                lights[a][b]=1
            del switches[(r,c)]
        
        for i in range(4):
            rr=r+dr[i]
            cc=c+dc[i]
            if 0<=rr<N and 0<=cc<N and not visited[rr][cc] and lights[rr][cc]:
                q.append([rr,cc])
                visited[rr][cc]=1

tmp1=1
while True:
    bfs(0,0)
    tmp2=0
    for i in range(N):
        for j in range(N):
            if lights[i][j]:
                tmp2+=1
    
    if tmp1==tmp2:
        print(tmp1)
        exit(0)
    else:
        tmp1=tmp2
