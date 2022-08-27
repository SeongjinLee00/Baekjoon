from collections import deque

T=int(input())

for _ in range(T):
    N,M=map(int,input().split())

    board=[['.']*(M+2)]

    for _ in range(N):
        board.append(['.']+list(input())+['.'])

    board.append(['.']*(M+2))

    dr=[1,-1,0,0]
    dc=[0,0,1,-1]

    start=[]

    for i in range(N+2):
        for j in range(M+2):
            if board[i][j]=='$':
                start.append([i,j])

    def bfs(r,c):
        costs=[[-1]*(M+2) for _ in range(N+2)]
        q=deque([[r,c,0]])
        costs[r][c]=0

        while q:
            r,c,d=q.popleft()
            for i in range(4):
                rr=r+dr[i]
                cc=c+dc[i]
                if 0<=rr<N+2 and 0<=cc<M+2 and costs[rr][cc]==-1:
                    if board[rr][cc]=='*':
                        continue
                    elif board[rr][cc]=='#':
                        q.append([rr,cc,d+1])
                        costs[rr][cc]=d+1
                    else:
                        q.appendleft([rr,cc,d])
                        costs[rr][cc]=d

        return costs

    c1=bfs(start[0][0],start[0][1])
    c2=bfs(start[1][0],start[1][1])
    c3=bfs(0,0)

    ans=[[0]*(M+2) for _ in range(N+2)]
    for i in range(N+2):
        for j in range(M+2):
            ans[i][j]=c1[i][j]+c2[i][j]+c3[i][j]
            if board[i][j]=='#':
                ans[i][j]-=2
    ret=99999999999
    for i in range(N+2):
        for j in range(M+2):
            if ans[i][j]<=-3:
                continue
            if ans[i][j]<ret:
                ret=ans[i][j]

    print(ret)