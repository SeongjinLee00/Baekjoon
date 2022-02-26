from collections import deque

import copy
N=int(input())

area=[]
for _ in range(N):
    area.append(list(input()))
area2=copy.deepcopy(area)
for i in range(N):
    for j in range(N):
        if area2[i][j]=='G':
            area2[i][j]='R'
dr=[1,-1,0,0]
dc=[0,0,1,-1]
cnt=0
cnt2=0
def bfs(r,c):
    global cnt
    q=deque([[r,c]])
    my_color=area[r][c]
    area[r][c]=0
    cnt+=1
    while q:
        r,c=q.popleft()
        for i in range(4):
            rr=r+dr[i]
            cc=c+dc[i]
            if 0<=rr<N and 0<=cc<N and area[rr][cc]==my_color:
                q.append([rr,cc])
                area[rr][cc]=0

def bfs2(r,c):
    global cnt2
    q=deque([[r,c]])
    my_color=area2[r][c]
    area2[r][c]=0
    cnt2+=1
    while q:
        r,c=q.popleft()
        for i in range(4):
            rr=r+dr[i]
            cc=c+dc[i]
            if 0<=rr<N and 0<=cc<N and area2[rr][cc]==my_color:
                q.append([rr,cc])
                area2[rr][cc]=0

for i in range(N):
    for j in range(N):
        if area[i][j]!=0:
            bfs(i,j)
print(cnt,end=' ')

for i in range(N):
    for j in range(N):
        if area2[i][j]!=0:
            bfs2(i,j)
print(cnt2)