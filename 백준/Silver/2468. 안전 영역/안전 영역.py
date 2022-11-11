from collections import deque

ans=1

N=int(input())
numbers=[]

for _ in range(N):
    numbers.append(list(map(int,input().split())))

memory=[row[:] for row in numbers]

dr=[1,-1,0,0]
dc=[0,0,1,-1]

def bfs(i,j):
    q=deque([[i,j]])

    while q:
        r,c=q.popleft()
        for i in range(4):
            rr=r+dr[i]
            cc=c+dc[i]

            if 0<=rr<N and 0<=cc<N and not visited[rr][cc] and type(numbers[rr][cc])==int:
                q.append([rr,cc])
                visited[rr][cc]=1

for k in range(1,101):
    numbers=[row[:] for row in memory]
    for i in range(N):
        for j in range(N):
            if numbers[i][j]<=k:
                numbers[i][j]='X'
    
    visited=[[0]*N for _ in range(N)]

    cnt=0
    for i in range(N):
        for j in range(N):
            if type(numbers[i][j])==int and not visited[i][j]:
                visited[i][j]=1
                bfs(i,j)
                cnt+=1
    
    ans=max(ans,cnt)

print(ans)