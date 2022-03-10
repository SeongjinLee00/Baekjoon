from collections import deque

N,M=map(int,input().split())

cheese=[]
for _ in range(N):
    cheese.append(list(map(int,input().split())))

dr=[1,-1,0,0]
dc=[0,0,1,-1]

def bfs():
    q=deque([[0,0]])
    visited=[[0]*M for _ in range(N)]
    melt=[]
    while q:
        r,c=q.popleft()
        visited[r][c]=1
        for i in range(4):
            rr=r+dr[i]
            cc=c+dc[i]
            if 0<=rr<N and 0<=cc<M and not visited[rr][cc]:
                if cheese[rr][cc]==0:
                    q.append([rr,cc])
                    visited[rr][cc]=1
                elif cheese[rr][cc]==1:
                    melt.append([rr,cc])
    return melt

cheesenum=[sum(sum(cheese,[]))]
while sum(sum(cheese,[]))>0:
    meltlist=bfs()

    for i in range(len(meltlist)):
        cheese[meltlist[i][0]][meltlist[i][1]]=0

    cheesenum.append(sum(sum(cheese,[])))

print(len(cheesenum)-1)
print(cheesenum[-2])