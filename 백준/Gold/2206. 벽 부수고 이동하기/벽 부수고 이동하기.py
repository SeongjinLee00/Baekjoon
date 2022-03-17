from collections import deque

N,M=map(int,input().split())
maze=[]

for _ in range(N):
    maze.append(list(map(int,list(input()))))

visited=[[0]*M for _ in range(N)]
visited_break=[[0]*M for _ in range(N)]
q=deque([[0,0,0,0]])
visited[0][0]=1

dr=[1,-1,0,0]
dc=[0,0,1,-1]

distances=[]
while q:
    r,c,d,b=q.popleft()
    if r==N-1 and c==M-1:
        print(d+1)
        exit(0)
    for i in range(4):
        rr=r+dr[i]
        cc=c+dc[i]
        if 0<=rr<N and 0<=cc<M:
            if b==0:
                if maze[rr][cc]==1 and not visited_break[rr][cc]:
                    q.append([rr,cc,d+1,1])
                    visited_break[rr][cc]=1
                if maze[rr][cc]==0 and not visited[rr][cc]:
                    q.append([rr,cc,d+1,0])
                    visited[rr][cc]=1
            
            if b==1:
                if maze[rr][cc]==1:
                    continue
                if maze[rr][cc]==0 and not visited_break[rr][cc]:
                    q.append([rr,cc,d+1,1])
                    visited_break[rr][cc]=1

if len(distances)>=1:
    print(min(distances))
else:
    print(-1)