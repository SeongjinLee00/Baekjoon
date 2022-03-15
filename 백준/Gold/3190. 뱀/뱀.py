from collections import deque
from pprint import pprint
N=int(input())

board=[[0]*N for _ in range(N)]
board[0][0]=9
K=int(input())

for _ in range(K):
    i,j=map(int,input().split())
    board[i-1][j-1]=1

rotations=deque()
L=int(input())
for _ in range(L):
    t,d=input().split()
    t=int(t)
    rotations.append([t,d])

dr=[-1,0,1,0]
dc=[0,1,0,-1]
snake=deque([[0,0]])
dir=1
time=0
temp=0
while True:

    if len(rotations)==0:
        while True:

            time+=1
            head_r,head_c=snake[0]
            new_head_r=head_r+dr[dir]
            new_head_c=head_c+dc[dir]
            if new_head_r==N or new_head_r==-1 or new_head_c==N or new_head_c==-1 or [new_head_r,new_head_c] in snake:
                print(time)
                exit(0)
            if board[new_head_r][new_head_c]==1:
                pass
            else:
                snake.pop()
            snake.appendleft([new_head_r,new_head_c])
    move, rot=rotations.popleft()
    while time<move:

        time+=1
        head_r,head_c=snake[0]
        new_head_r=head_r+dr[dir]
        new_head_c=head_c+dc[dir]
        if new_head_r==N or new_head_r==-1 or new_head_c==N or new_head_c==-1 or [new_head_r,new_head_c] in snake:
            print(time)
            exit(0)
        if board[new_head_r][new_head_c]==1:
            board[new_head_r][new_head_c]=0
        else:
            snake.pop()
        snake.appendleft([new_head_r,new_head_c])
    
    if rot=='D':
        dir+=1
    elif rot=='L':
        dir-=1
    dir=dir%4
    temp=move