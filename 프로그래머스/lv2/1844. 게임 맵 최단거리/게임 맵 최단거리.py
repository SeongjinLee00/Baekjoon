from collections import deque

def solution(maps):
    R=len(maps)
    C=len(maps[0])
    q=deque([[0,0,1]])
    visited=[[0]*C for _ in range(R)]
    visited[0][0]=1
    dr=[1,-1,0,0]
    dc=[0,0,1,-1]
    
    while q:
        r,c,d=q.popleft()
        if r==R-1 and c==C-1:
            return d
        for i in range(4):
            rr=r+dr[i]
            cc=c+dc[i]
            if 0<=rr<R and 0<=cc<C and not visited[rr][cc] and maps[rr][cc]:
                visited[rr][cc]=1
                q.append([rr,cc,d+1])
    return -1