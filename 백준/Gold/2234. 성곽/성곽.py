from collections import deque

M,N=map(int,input().split())

numbers=[]

for _ in range(N):
    numbers.append(list(map(int,input().split())))

room=[[[0,0,0,0] for _ in range(M)] for _ in range(N)]

# 0 1 2 3 서 북 동 남
for i in range(N):
    for j in range(M):
        if numbers[i][j]>=8:
            numbers[i][j]-=8
            room[i][j][3]=1
        if numbers[i][j]>=4:
            numbers[i][j]-=4
            room[i][j][2]=1
        if numbers[i][j]>=2:
            numbers[i][j]-=2
            room[i][j][1]=1
        if numbers[i][j]>=1:
            numbers[i][j]-=1
            room[i][j][0]=1

visited=[[0]*M for _ in range(N)]

dr=[0,-1,0,1]
dc=[-1,0,1,0]

def get_area(r,c):
    q=deque([[r,c]])
    area=1
    visited[r][c]=1

    while q:
        r,c=q.popleft()
        for i in range(4):
            rr=r+dr[i]
            cc=c+dc[i]
            if (i==0 and room[r][c][0]==0) or (i==1 and room[r][c][1]==0) or (i==2 and room[r][c][2]==0) or (i==3 and room[r][c][3]==0):
                if 0<=rr<N and 0<=cc<M and not visited[rr][cc]:
                    q.append([rr,cc])
                    visited[rr][cc]=1
                    area+=1
    
    return area

cnt=0
max_area=0
for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            cnt+=1
            max_area=max(max_area,get_area(i,j))
print(cnt)
print(max_area)

for i in range(N):
    for j in range(M):
        for k in range(4):
            if room[i][j][k]==1:
                room[i][j][k]=0
                visited=[[0]*M for _ in range(N)]
                max_area=max(max_area,get_area(i,j))
                room[i][j][k]=1

print(max_area)