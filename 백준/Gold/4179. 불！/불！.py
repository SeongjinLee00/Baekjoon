from collections import deque
from pprint import pprint

R,C=map(int,input().split())

maze=[]

for _ in range(R):
    maze.append(list(input()))

for i in range(R):
    for j in range(C):
        if maze[i][j]=='J' and (i==0 or i==R-1 or j==0 or j==C-1):
            print(1)
            exit(0)

J=0 # 지훈
fire=[]
for i in range(R):
    for j in range(C):
        if maze[i][j]=='J':
            S=[i,j]
            maze[i][j]='.'
        if maze[i][j]=='F':
            fire.append([i,j])

dr=[1,-1,0,0]
dc=[0,0,1,-1]

visited=[[0]*C for _ in range(R)]
def bfs_fire():
    q=deque()
    for i in range(len(fire)):
        q.append([fire[i][0],fire[i][1],0])
        visited[fire[i][0]][fire[i][1]]=1

    while q:
        r,c,d=q.popleft()
        for i in range(4):
            rr=r+dr[i]
            cc=c+dc[i]
            if 0<=rr<R and 0<=cc<C and maze[rr][cc]=='.' and not visited[rr][cc]:
                visited[rr][cc]=1
                q.append([rr,cc,d+1])
                maze[rr][cc]=d+1

bfs_fire()

visited2=[[0]*C for _ in range(R)]
def bfs():
    q=deque([[S[0],S[1],0]])
    visited2[S[0]][S[1]]=1

    while q:
        r,c,d=q.popleft()
        for i in range(4):
            rr=r+dr[i]
            cc=c+dc[i]
            if 0<=rr<R and 0<=cc<C and maze[rr][cc]!='#' and not visited2[rr][cc]:
                if type(maze[rr][cc])==int: # # . 
                    if maze[rr][cc]>d+1:
                        visited2[rr][cc]=1
                        q.append([rr,cc,d+1])
                        if rr==0 or rr==R-1 or cc==0 or cc==C-1:
                            return d+2
                elif maze[rr][cc]=='.':
                    visited2[rr][cc]=1
                    q.append([rr,cc,d+1])            
                    if rr==0 or rr==R-1 or cc==0 or cc==C-1:
                        return d+2

    return 'IMPOSSIBLE'

print(bfs())