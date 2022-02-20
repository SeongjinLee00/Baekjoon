from collections import deque
import sys
sys.setrecursionlimit(10**9)

N,M=map(int,input().split())

board=[]
for _ in range(N):
    board.append(list(input()))

ans=0
dr=[-1,1]
dc=[-1,1]

def dfs(r,c):

    if board[r][c]=='|':
        board[r][c]='o'
        for i in range(2):
            rr=r+dr[i]
            if 0<=rr<N and board[rr][c]=='|':
                dfs(rr,c)

    if board[r][c]=='-':
        board[r][c]='o'
        for i in range(2):
            cc=c+dc[i]
            if 0<=cc<M and board[r][cc]=='-':
                dfs(r,cc)

for i in range(N):
    for j in range(M):
        if board[i][j]=='|' or board[i][j]=='-':
            dfs(i,j)
            ans+=1

print(ans)