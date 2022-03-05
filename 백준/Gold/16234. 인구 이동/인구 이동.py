from collections import deque

N,L,R=map(int,input().split())

populations=[]

for _ in range(N):
    populations.append(list(map(int,input().split())))

dr=[1,-1,0,0]
dc=[0,0,1,-1]
visited=[[0]*N for _ in range(N)]
union=[]

def bfs(r,c):
    q=deque([[r,c]])
    visited[r][c]=1
    union.append([r,c])
    while q:
        r,c=q.popleft()
        for i in range(4):
            rr=r+dr[i]
            cc=c+dc[i]
            if 0<=rr<N and 0<=cc<N and L<=abs(populations[rr][cc]-populations[r][c])<=R and not visited[rr][cc]:
                visited[rr][cc]=1
                union.append([rr,cc])
                q.append([rr,cc])

s=0
a=0
day=0
while True:
    flag=0
    for r in range(N):
        for c in range(N):
            if not visited[r][c]:
                union=[]
                bfs(r,c)
            if len(union)<=1:
                pass
            else:
                flag=1
                for country in union:
                    s+=populations[country[0]][country[1]]
                a=s//len(union)
                for country in union:
                    populations[country[0]][country[1]]=a
                s=0
                a=0
    if flag==0:
        print(day)
        exit(0)
    visited=[[0]*N for _ in range(N)]
    day+=1