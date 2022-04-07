from collections import deque

N,M=map(int,input().split())

ice=[]

for _ in range(N):
    ice.append(list(map(int,input().split())))

dr=[1,-1,0,0]
dc=[0,0,1,-1]

def bfs(r,c):
    q=deque([[r,c]])
    visited[r][c]=1
    while q:
        r,c=q.popleft()
        for i in range(4):
            rr=r+dr[i]
            cc=c+dc[i]
            if 0<=rr<N and 0<=cc<M:
                if ice[rr][cc]>=1 and not visited[rr][cc]:
                    q.append([rr,cc])
                    visited[rr][cc]=1
                if ice[rr][cc]==0:
                    meltlist[r][c]+=1

from pprint import pprint
time=0
total=0
for i in range(N):
    for j in range(M):
        total+=ice[i][j]
while total>0:
    total=0
    time+=1
    cnt=0
    visited=[[0]*M for _ in range(N)]
    meltlist=[[0]*M for _ in range(N)]
    
    for i in range(N):
        for j in range(M):
            if ice[i][j]>=1 and not visited[i][j]:
                if cnt:
                    print(time-1)
                    exit(0)
                else:
                    cnt+=1
                    bfs(i,j)
    
    for i in range(N):
        for j in range(M):
            ice[i][j]=max(0,ice[i][j]-meltlist[i][j])
    
    for i in range(N):
        for j in range(M):
            total+=ice[i][j]

print(0)