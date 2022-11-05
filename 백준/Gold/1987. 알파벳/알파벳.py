from collections import deque

R,C=map(int,input().split())

board=[]

for _ in range(R):
    board.append(list(input()))

q=deque([[0,0,board[0][0]]])

dr=[1,-1,0,0]
dc=[0,0,1,-1]

ans=0
while q:
    r,c,s=q.pop()
    if len(s)>ans:
        ans=len(s)
    for i in range(4):
        rr=r+dr[i]
        cc=c+dc[i]
        if 0<=rr<R and 0<=cc<C and board[rr][cc] not in s:
            q.append([rr,cc,s+board[rr][cc]])

print(ans)