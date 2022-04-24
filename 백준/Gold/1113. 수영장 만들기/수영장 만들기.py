from collections import deque

N,M=map(int,input().split())

wall=[]

for _ in range(N):
    wall.append(list(map(int,list(input()))))

maxheight=0
for i in range(N):
    for j in range(M):
        if wall[i][j]>maxheight:
            maxheight=wall[i][j]

water=[[maxheight]*M for _ in range(N)]

ans=0

for i in range(N):
    for j in range(M):
        ans+=maxheight-wall[i][j]

dr=[1,-1,0,0]
dc=[0,0,1,-1]

def flow(i,j):
    global ans
    visited=[[0]*M for _ in range(N)]
    q=deque([[i,j]])
    visited[i][j]=1
    waterheight=water[i][j]

    while q:
        r,c=q.popleft()
        for k in range(4):
            rr=r+dr[k]
            cc=c+dc[k]
            if rr==-1 or rr==N or cc==-1 or cc==M:
                water[i][j]-=1
                ans-=1
                return
            if 0<=rr<N and 0<=cc<M and not visited[rr][cc] and waterheight>wall[rr][cc]:
                q.append([rr,cc])
                visited[rr][cc]=1

for h in range(9,1,-1):
    for i in range(N):
        for j in range(M):
            if water[i][j]==h and water[i][j]>wall[i][j]:
                flow(i,j)

print(ans)