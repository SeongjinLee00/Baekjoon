from collections import deque

T=int(input())

for _ in range(T):
    N=int(input())
    start,end=map(int,input().split())
    goalx,goaly=map(int,input().split())

    visited=[[0]*N for _ in range(N)]

    dr=[1,1,2,2,-1,-1,-2,-2]
    dc=[2,-2,1,-1,2,-2,1,-1]
    
    def bfs(r,c):
        q=deque([[r,c,0]])
        visited[r][c]=0

        while q:
            r,c,move=q.popleft()
            if r==goalx and c==goaly:
                return move
            for i in range(8):
                rr=r+dr[i]
                cc=c+dc[i]
                if 0<=rr<N and 0<=cc<N and not visited[rr][cc]:
                    visited[rr][cc]=1
                    q.append([rr,cc,move+1])

    print(bfs(start,end))