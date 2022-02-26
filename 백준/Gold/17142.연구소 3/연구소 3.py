from collections import deque
from itertools import combinations

N,M=map(int,input().split())
area=[]

for _ in range(N):
    area.append(list(map(int,input().split())))

area2=[item[:] for item in area]
candidate=[]
for i in range(N):
    for j in range(N):
        if area[i][j]==2:
            candidate.append([i,j])
dr=[1,-1,0,0]
dc=[0,0,1,-1]
q=deque()
def bfs():
    while q:
        r,c,d=q.popleft()
        for i in range(4):
            rr=r+dr[i]
            cc=c+dc[i]
            if 0<=rr<N and 0<=cc<N and area[rr][cc]==0 and not visited[rr][cc]:
                visited[rr][cc]=1
                distances[rr][cc]=d+1
                q.append([rr,cc,d+1])
            elif 0<=rr<N and 0<=cc<N and area[rr][cc]=='*' and not visited[rr][cc]:
                visited[rr][cc]=1
                distances[rr][cc]=d+1
                q.append([rr,cc,d+1])

maxd=[]
for ch in combinations(candidate,M):
    area=[item[:] for item in area2]
    visited=[[0]*N for _ in range(N)]
    distances=[[-1]*N for _ in range(N)]
    
    for dead in candidate:
        area[dead[0]][dead[1]]='*'
    for alive in ch:
        area[alive[0]][alive[1]]=2
        q.append([alive[0],alive[1],0])
        visited[alive[0]][alive[1]]=1
        distances[alive[0]][alive[1]]=0
    
    bfs()
    
    for i in range(N):
        for j in range(N):
            if area[i][j]=='*':
                distances[i][j]=0
    fail=False
    for i in range(N):
        for j in range(N):
            if distances[i][j]==-1 and area[i][j]==0:
                maxd.append(-1)
                fail=True
    if not fail:
        maxd.append(max(sum(distances,[])))

maxd.sort()
if maxd[-1]==-1:
    print(-1)
else:
    for mm in maxd:
        if mm>=0:
            print(mm)
            exit(0)