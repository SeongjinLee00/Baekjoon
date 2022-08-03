from collections import deque

N=int(input())
board=[]

for _ in range(N):
    board.append(list(input()))

cnt=0
for i in range(N):
    for j in range(N):
        if board[i][j]=='B':
            cnt+=1
        if cnt==2:
            start=[i,j]
            break
    if cnt==2:
        break

if board[i][j-1]=='B':
    configuration=1 # 가로
    board[i][j-1], board[i][j], board[i][j+1] = 0, 0, 0
else:
    configuration=-1 # 세로
    board[i+1][j], board[i][j], board[i-1][j] = 0, 0, 0

cnt=0
for i in range(N):
    for j in range(N):
        if board[i][j]=='E':
            cnt+=1
        if cnt==2:
            end=[i,j]
            break
    if cnt==2:
        break

if board[i][j-1]=='E':
    end_configuration=1 # 가로
    board[i][j-1], board[i][j], board[i][j+1] = 0, 0, 0
else:
    end_configuration=-1 # 세로
    board[i+1][j], board[i][j], board[i-1][j] = 0, 0, 0

dr=[1,-1,0,0,0]
dc=[0,0,1,-1,0]
dconfi=[1,1,1,1,-1]

q=deque([[start[0],start[1],0,configuration]])
visited_garo=[[0]*N for _ in range(N)]
visited_sero=[[0]*N for _ in range(N)]

if configuration==1:
    visited_garo[start[0]][start[1]]=1
else:
    visited_sero[start[0]][start[1]]=1

while q:
    r,c,d,configuration=q.popleft()
    if r==end[0] and c==end[1] and configuration==end_configuration:
        print(d)
        exit(0)
    for i in range(5):
        rr=r+dr[i]
        cc=c+dc[i]
        configuration=configuration*dconfi[i]
        if 0<=i<=3:
            if configuration==1:
                if 0<=rr<N and 1<=cc<N-1 and (board[rr][cc-1]!='1' and board[rr][cc]!='1' and board[rr][cc+1]!='1') and not visited_garo[rr][cc]:
                    visited_garo[rr][cc]=1
                    q.append([rr,cc,d+1,configuration])
            elif configuration==-1:
                if 1<=rr<N-1 and 0<=cc<N and (board[rr-1][cc]!='1' and board[rr][cc]!='1' and board[rr+1][cc]!='1') and not visited_sero[rr][cc]:
                    visited_sero[rr][cc]=1
                    q.append([rr,cc,d+1,configuration])
        
        elif i==4:
            if 1<=rr<N-1 and 1<=cc<N-1 and (board[rr-1][cc-1]!='1' and board[rr-1][cc]!='1' and board[rr-1][cc+1]!='1' and board[rr][cc-1]!='1' and board[rr][cc]!='1' and board[rr][cc+1]!='1' and board[rr+1][cc-1]!='1' and board[rr+1][cc]!='1' and board[rr+1][cc+1]!='1'):
                if configuration==-1 and not visited_sero[rr][cc]:
                    visited_sero[rr][cc]=1
                    q.append([rr,cc,d+1,configuration])
                elif configuration==1 and not visited_garo[rr][cc]:
                    visited_garo[rr][cc]=1
                    q.append([rr,cc,d+1,configuration])

print(0)