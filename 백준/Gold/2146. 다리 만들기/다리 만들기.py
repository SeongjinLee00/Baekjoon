from collections import deque
from pprint import pprint

N=int(input())

island=[]
for _ in range(N):
    island.append(list(map(int,input().split())))

dr=[1,-1,0,0]
dc=[0,0,1,-1]

visited=[[0]*N for _ in range(N)]

islet=[]
def union(i,j):
    q=deque([[i,j]])
    visited[i][j]=1
    islet.append([i,j,0])
    
    while q:
        r,c=q.popleft()
        for i in range(4):
            rr=r+dr[i]
            cc=c+dc[i]
            if 0<=rr<N and 0<=cc<N and island[rr][cc]==1 and not visited[rr][cc]:
                q.append([rr,cc])
                visited[rr][cc]=1
                islet.append([rr,cc,0])

result=[]
for i in range(N):
    for j in range(N):
        build=False
        if island[i][j]==1 and not visited[i][j]:
            union(i,j)
            visited2=[[0]*N for _ in range(N)]
            
            q=deque(islet)
            while q:
                r,c,d=q.popleft()
                for i in range(4):
                    rr=r+dr[i]
                    cc=c+dc[i]
                    if 0<=rr<N and 0<=cc<N and island[rr][cc]==0 and not visited2[rr][cc]:
                        q.append([rr,cc,d+1])
                        visited2[rr][cc]=1
                    if 0<=rr<N and 0<=cc<N and island[rr][cc]==1 and not visited[rr][cc]:
                        result.append(d)
                        build=True
                        break
                if build:
                    break
            islet=[]

print(min(result))