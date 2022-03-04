from collections import deque

N,K=map(int,input().split())

area=[]

for _ in range(N):
    area.append(list(map(int,input().split())))
S,R,C=map(int,input().split())
virus=[]

for i in range(N):
    for j in range(N):
        if area[i][j]>=1:
            virus.append([i,j,area[i][j],0])

virus.sort(key=lambda x:x[2])


dr=[1,-1,0,0]
dc=[0,0,1,-1]
time=0
q=deque(virus)

while q:
    r,c,species,d=q.popleft()
    if d==S:
        break
    for i in range(4):
        rr=r+dr[i]
        cc=c+dc[i]
        if 0<=rr<N and 0<=cc<N and area[rr][cc]==0:
            area[rr][cc]=species
            q.append([rr,cc,species,d+1])

print(area[R-1][C-1])