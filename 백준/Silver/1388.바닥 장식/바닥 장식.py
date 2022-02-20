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
visited=[[0]*M for _ in range(N)]

def dfs(r,c):
    if board[r][c]=='|':
        visited[r][c]=1
        for i in range(2):
            rr=r+dr[i]
            if 0<=rr<N and board[rr][c]=='|' and not visited[rr][c]:
                dfs(rr,c)

    if board[r][c]=='-':
        visited[r][c]=1
        for i in range(2):
            cc=c+dc[i]
            if 0<=cc<M and board[r][cc]=='-' and not visited[r][cc]:
                dfs(r,cc)

for i in range(N):
    for j in range(M):
        if (board[i][j]=='|' or board[i][j]=='-') and not visited[i][j]:
            dfs(i,j)
            ans+=1

print(ans)