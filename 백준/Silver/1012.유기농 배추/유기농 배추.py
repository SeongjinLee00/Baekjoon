import sys
from collections import deque

T=int(input())

for _ in range(T):
    M,N,K=map(int,input().split())

    area=[[0]*M for _ in range(N)]

    for _ in range(K):
        x,y=map(int,sys.stdin.readline().split())

        area[y][x]=1
    
    dr=[1,-1,0,0]
    dc=[0,0,1,-1]

    def bfs(r,c):
        area[r][c]=2
        q=deque([[r,c]])
        while q:
            r,c=q.popleft()
            for i in range(4):
                rr=r+dr[i]
                cc=c+dc[i]
                if 0<=rr<N and 0<=cc<M and area[rr][cc]==1:
                    area[rr][cc]=2
                    q.append([rr,cc])

    cnt=0
    for i in range(N): # M이 가로길이, N이 세로길이
        for j in range(M):
            if area[i][j]==1:
                bfs(i,j)
                cnt+=1

    print(cnt)