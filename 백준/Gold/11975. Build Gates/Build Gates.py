from collections import deque

field = [[0]*4004 for _ in range(4004)]
N=int(input())
path=input()

r=2002
c=2002

dr=[1,-1,0,0]
dc=[0,0,1,-1]

def bfs(r,c):
    q=deque([[r,c]])
    field[r][c]=1

    while q:
        r,c=q.popleft()
        for i in range(4):
            rr=r+dr[i]
            cc=c+dc[i]
            if not field[rr][cc]:
                field[rr][cc]=1
                q.append([rr,cc])

field[r][c]=1
for p in path:
    if p=='N':
        r-=1
        field[r][c]=1
        r-=1
    elif p=='S':
        r+=1
        field[r][c]=1
        r+=1
    elif p=='E':
        c+=1
        field[r][c]=1
        c+=1
    elif p=='W':
        c-=1
        field[r][c]=1
        c-=1

    field[r][c]=1

ans=0
for i in range(4004):
    for j in range(4004):
        if not field[i][j]:
            bfs(i,j)
            ans+=1

print(ans-1)