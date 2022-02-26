from collections import deque

R,C=map(int,input().split())

forest=[]

for _ in range(R):
    forest.append(list(input()))

S=0 # 고슴도치
D=0 # 동굴
water=[]
for i in range(R):
    for j in range(C):
        if forest[i][j]=='S':
            S=[i,j]
        if forest[i][j]=='D':
            D=[i,j]
        if forest[i][j]=='*':
            water.append([i,j])
            forest[i][j]=0

dr=[1,-1,0,0]
dc=[0,0,1,-1]

visited=[[0]*C for _ in range(R)]
def bfs_water():
    q=deque()
    for i in range(len(water)):
        q.append([water[i][0],water[i][1],0])
        visited[water[i][0]][water[i][1]]=1

    while q:
        r,c,d=q.popleft()
        for i in range(4):
            rr=r+dr[i]
            cc=c+dc[i]
            if 0<=rr<R and 0<=cc<C and forest[rr][cc]=='.' and not visited[rr][cc]:
                visited[rr][cc]=1
                q.append([rr,cc,d+1])
                forest[rr][cc]=d+1

bfs_water()

visited2=[[0]*C for _ in range(R)]
def bfs():
    q=deque([[S[0],S[1],0]])
    visited2[S[0]][S[1]]=1

    while q:
        r,c,d=q.popleft()
        for i in range(4):
            rr=r+dr[i]
            cc=c+dc[i]
            if 0<=rr<R and 0<=cc<C and forest[rr][cc]!='X' and not visited2[rr][cc]:
                if type(forest[rr][cc])==int:
                    if forest[rr][cc]>d+1:
                        visited2[rr][cc]=1
                        q.append([rr,cc,d+1])
                elif forest[rr][cc]=='.':
                    visited2[rr][cc]=1
                    q.append([rr,cc,d+1])                    
                elif forest[rr][cc]=='D':
                    return d+1
    return 'KAKTUS'

print(bfs())