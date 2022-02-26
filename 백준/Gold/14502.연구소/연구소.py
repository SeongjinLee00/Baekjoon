from collections import deque
from itertools import combinations
import copy

N,M=map(int,input().split())

area=[]

for _ in range(N):
    area.append(list(map(int,input().split())))

area2=copy.deepcopy(area)
candidates=[]
virus=[]
for i in range(N):
    for j in range(M):
        if area[i][j]==0:
            candidates.append([i,j])
        elif area[i][j]==2:
            virus.append([i,j])
    
a=combinations(candidates,3)

dr=[1,-1,0,0]
dc=[0,0,1,-1]
def bfs(r,c):
    q=deque([[r,c]])
    while q:
        r,c=q.popleft()
        for i in range(4):
            rr=r+dr[i]
            cc=c+dc[i]
            if 0<=rr<N and 0<=cc<M and area[rr][cc]==0:
                area[rr][cc]=2
                q.append([rr,cc])
max=0
for ch in a:
    area=[item[:] for item in area2]
    area[ch[0][0]][ch[0][1]]=1
    area[ch[1][0]][ch[1][1]]=1
    area[ch[2][0]][ch[2][1]]=1
    
    for i in range(len(virus)):
        bfs(virus[i][0],virus[i][1])
    cnt=sum(area,[]).count(0)

    if cnt>max:
        max=cnt

print(max)