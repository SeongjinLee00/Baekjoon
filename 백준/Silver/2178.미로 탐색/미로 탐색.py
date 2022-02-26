from collections import deque

N,M=map(int,input().split())

maze=[]
for _ in range(N):
    maze.append(list(input()))

dr=[1,-1,0,0]
dc=[0,0,1,-1]
def bfs():
    q=deque([[0,0,1]])
    maze[0][0]='X'

    while q:
        r,c,d=q.popleft()
        for i in range(4):
            rr=r+dr[i]
            cc=c+dc[i]
            if 0<=rr<N and 0<=cc<M and maze[rr][cc]=='1':
                maze[rr][cc]='X'
                q.append([rr,cc,d+1])
            if rr==N-1 and cc==M-1:
                return d+1

print(bfs())