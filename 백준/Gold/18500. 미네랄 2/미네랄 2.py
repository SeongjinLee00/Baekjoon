from collections import deque

N,M=map(int,input().split())

board=[]

for _ in range(N):
    board.append(list(input()))

dr=[1,0,0,-1]
dc=[0,1,-1,0]
def cluster(r,c):
    q=deque([[r,c]])
    visited[r][c]=1
    clusters=[[r,c]]
    flag=0

    while q:
        r,c=q.popleft()
        if r==N-1:
            flag=1
        for i in range(4):
            rr=r+dr[i]
            cc=c+dc[i]
            if 0<=rr<N and 0<=cc<M and not visited[rr][cc] and board[rr][cc]=='x':
                q.append([rr,cc])
                visited[rr][cc]=1
                clusters.append([rr,cc])
    
    return False if flag else True, clusters

def attack(h,d):
    if d==1:
        c=0

        while board[N-h][c]=='.':
            c+=1
            if c==M:
                return
        board[N-h][c]='.'
    elif d==2:
        c=M-1

        while board[N-h][c]=='.':
            c-=1
            if c==-1:
                return
        board[N-h][c]='.'
    
T=int(input())

heights=list(map(int,input().split()))

for turn in range(T):
    attack(heights[turn], 1 if turn%2==0 else 2)

    visited=[[0]*M for _ in range(N)]

    worked=0

    for i in range(N):
        for j in range(M):
            if board[i][j]=='x' and not visited[i][j]:
                is_cluster, clusters = cluster(i,j)
                while True:
                    if not is_cluster:
                        break
                    for item in clusters:
                        board[item[0]][item[1]]='.'
                    for item in clusters:
                        item[0]+=1
                        board[item[0]][item[1]]='x'
                        if item[0]==N-1 or board[item[0]+1][item[1]]=='x':
                            is_cluster=False
                    if not is_cluster:
                        worked=1
                        break
            if worked:
                break

        if worked:
            break

for row in board:
    print("".join(row))