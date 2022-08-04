from pprint import pprint
from collections import deque

N,M=map(int,input().split())

board=[]

for _ in range(N):
    board.append(list(input()))

for i in range(N):
    for j in range(M):
        if board[i][j]=='R':
            red=[i,j]
        elif board[i][j]=='B':
            blue=[i,j]

# 0 1 2 3 하 상 우 좌
board[red[0]][red[1]]='.'
board[blue[0]][blue[1]]='.'
q=deque([[red[0],red[1],blue[0],blue[1],0,-1]])
fail=False
success=False
visited=set()
while q:
    Rr,Rc,Br,Bc,d,last_direction=q.popleft()
    if d==10:
        print(0)
        exit(0)
    memory=[Rr,Rc,Br,Bc,d,last_direction]

    ############# 아래로 이동하기
    if last_direction!=0:
        if Rr>Br:
            while True:
                Rr+=1
                if board[Rr][Rc]=='O':
                    success=True
                    break
                if board[Rr][Rc]=='#':
                    Rr-=1
                    break
            while True:
                Br+=1
                if board[Br][Bc]=='O':
                    fail=True
                    break
                if board[Br][Bc]=='#' or (Br==Rr and Bc==Rc):
                    Br-=1
                    break
        else:
            while True:
                Br+=1
                if board[Br][Bc]=='O':
                    fail=True
                    break
                if board[Br][Bc]=='#':
                    Br-=1
                    break
            while True:
                Rr+=1
                if board[Rr][Rc]=='O':
                    success=True
                    break
                if board[Rr][Rc]=='#' or (Br==Rr and Bc==Rc):
                    Rr-=1
                    break
        if not fail and (Rr,Rc,Br,Bc) not in visited:
            q.append([Rr,Rc,Br,Bc,d+1,0])
            visited.add((Rr,Rc,Br,Bc))
            if success:
                print(1)
                exit(0)
        fail=False
        success=False
    
    ############### 위로 이동하기
    Rr,Rc,Br,Bc,d,last_direction=memory
    if last_direction!=1:
        if Rr<Br:
            while True:
                Rr-=1
                if board[Rr][Rc]=='O':
                    success=True
                    break
                if board[Rr][Rc]=='#':
                    Rr+=1
                    break
            while True:
                Br-=1
                if board[Br][Bc]=='O':
                    fail=True
                    break
                if board[Br][Bc]=='#' or (Br==Rr and Bc==Rc):
                    Br+=1
                    break
        else:
            while True:
                Br-=1
                if board[Br][Bc]=='O':
                    fail=True
                    break
                if board[Br][Bc]=='#':
                    Br+=1
                    break
            while True:
                Rr-=1
                if board[Rr][Rc]=='O':
                    success=True
                    break
                if board[Rr][Rc]=='#' or (Br==Rr and Bc==Rc):
                    Rr+=1
                    break
        if not fail and (Rr,Rc,Br,Bc) not in visited:
            q.append([Rr,Rc,Br,Bc,d+1,1])
            visited.add((Rr,Rc,Br,Bc))
            if success:
                print(1)
                exit(0)
        fail=False
        success=False

    ############ 오른쪽으로 이동하기
    Rr,Rc,Br,Bc,d,last_direction=memory
    if last_direction!=2:
        if Rc>Bc:
            while True:
                Rc+=1
                if board[Rr][Rc]=='O':
                    success=True
                    break
                if board[Rr][Rc]=='#':
                    Rc-=1
                    break
            while True:
                Bc+=1
                if board[Br][Bc]=='O':
                    fail=True
                    break
                if board[Br][Bc]=='#' or (Br==Rr and Bc==Rc):
                    Bc-=1
                    break
        else:
            while True:
                Bc+=1
                if board[Br][Bc]=='O':
                    fail=True
                    break
                if board[Br][Bc]=='#':
                    Bc-=1
                    break
            while True:
                Rc+=1
                if board[Rr][Rc]=='O':
                    success=True
                    break
                if board[Rr][Rc]=='#' or (Br==Rr and Bc==Rc):
                    Rc-=1
                    break
        if not fail and (Rr,Rc,Br,Bc) not in visited:
            q.append([Rr,Rc,Br,Bc,d+1,2])
            visited.add((Rr,Rc,Br,Bc))
            if success:
                print(1)
                exit(0)
        fail=False
        success=False

    ############ 왼쪽으로 이동하기
    Rr,Rc,Br,Bc,d,last_direction=memory
    if last_direction!=3:
        if Rc<Bc:
            while True:
                Rc-=1
                if board[Rr][Rc]=='O':
                    success=True
                    break
                if board[Rr][Rc]=='#':
                    Rc+=1
                    break
            while True:
                Bc-=1
                if board[Br][Bc]=='O':
                    fail=True
                    break
                if board[Br][Bc]=='#' or (Br==Rr and Bc==Rc):
                    Bc+=1
                    break
        else:
            while True:
                Bc-=1
                if board[Br][Bc]=='O':
                    fail=True
                    break
                if board[Br][Bc]=='#':
                    Bc+=1
                    break
            while True:
                Rc-=1
                if board[Rr][Rc]=='O':
                    success=True
                    break
                if board[Rr][Rc]=='#' or (Br==Rr and Bc==Rc):
                    Rc+=1
                    break

        if not fail and (Rr,Rc,Br,Bc) not in visited:
            q.append([Rr,Rc,Br,Bc,d+1,3])
            visited.add((Rr,Rc,Br,Bc))
            if success:
                print(1)
                exit(0)
        fail=False
        success=False

print(0)