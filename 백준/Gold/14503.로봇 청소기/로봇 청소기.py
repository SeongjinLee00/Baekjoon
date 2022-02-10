N,M=map(int,input().split())
r,c,d=map(int,input().split())
board=[]
vel_x, vel_y=0, 1
sight_x, sight_y=0, 1
cnt=0
for _ in range(N):
    board.append(list(map(int,input().split())))

def clean():
    global cnt
    board[r][c]=2
    cnt = cnt+1

def rotate(): # 방향을 전환하는 함수
    global d
    global vel_x
    global vel_y
    d=(d+3)%4
    if d==0:
        vel_x, vel_y=0, -1
    elif d==1:
        vel_x, vel_y=1, 0
    elif d==2:
        vel_x, vel_y=0, 1
    elif d==3:
        vel_x, vel_y=-1, 0

def move():
    global r
    global c
    c=c+vel_x
    r=r+vel_y

def seeleft():
    global sight_x
    global sight_y
    if d==0:
        sight_x, sight_y=-1,0
    elif d==1:
        sight_x, sight_y=0,-1
    elif d==2:
        sight_x, sight_y=1,0
    elif d==3:
        sight_x, sight_y=0,1

clean()

while True:
    seeleft() # 일단 왼쪽을 살펴
    if board[r+sight_y][c+sight_x]==0: # a, 청소하지 않은 공간이 있다면, 한 칸 이동후 청소
        rotate()
        move()
        sight_x, sight_y=vel_x, vel_y
        clean()

    elif board[r+1][c]!=0 and board[r][c+1]!=0 and board[r-1][c]!=0 and board[r][c-1]!=0 and board[r-vel_y][c-vel_x]==1: # d
        break

    elif board[r+1][c]!=0 and board[r][c+1]!=0 and board[r-1][c]!=0 and board[r][c-1]!=0: # c
        c=c-vel_x
        r=r-vel_y
        if board[r][c]==0:
            clean()

    elif board[r+sight_y][c+sight_x]!=0: # b, 청소할게 없다면 회전하고 2번을 반복
        rotate()

print(cnt)