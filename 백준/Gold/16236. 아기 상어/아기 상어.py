from collections import deque

N=int(input())

area=[]

for _ in range(N):
    area.append(list(map(int,input().split())))

for i in range(N):
    for j in range(N):
        if area[i][j]==9:
            curr_r=i
            curr_c=j
area[curr_r][curr_c]=0
dr=[1,-1,0,0]
dc=[0,0,1,-1]


size=2
cnt=0
time=0
prey=[]
def bfs(r,c):

    global prey
    prey=[]
    q=deque([[r,c,0]])
    visited=[[0]*N for _ in range(N)]
    visited[r][c]=1
    while q:
        r,c,d=q.popleft()
        for i in range(4):
            rr=r+dr[i]
            cc=c+dc[i]
            if 0<=rr<N and 0<=cc<N and area[rr][cc]<=size and not visited[rr][cc]:
                visited[rr][cc]=1
                q.append([rr,cc,d+1])
                if 1<=area[rr][cc]<size:
                    prey.append([rr,cc,d+1])

while True:
    bfs(curr_r,curr_c)
    if prey==[]:
        print(time)
        exit(0)
    else:
        prey.sort(key=lambda x:(x[2],x[0],x[1]))
        area[prey[0][0]][prey[0][1]]=0
        cnt+=1
        time+=prey[0][2]
        curr_r=prey[0][0]
        curr_c=prey[0][1]
        if cnt==size:
            size+=1
            cnt=0