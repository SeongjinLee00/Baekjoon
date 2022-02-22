from collections import deque

M,N=map(int,input().split()) # 가로로 M 세로로 N
tomato=[]
for _ in range(N):
    tomato.append(list(map(int,input().split())))

distances=[[9999999]*M for _ in range(N)]

dr=[1,-1,0,0]
dc=[0,0,1,-1]
q=deque()
visited=[[0]*M for _ in range(N)]
def bfs(r,c):
    while q:
        r,c,d=q.popleft()
        visited[r][c]=1
        if d<distances[r][c]:
            distances[r][c]=d
        for i in range(4):
            rr=r+dr[i]
            cc=c+dc[i]
            if 0<=rr<N and 0<=cc<M and not visited[rr][cc] and tomato[rr][cc]==0:
                visited[rr][cc]=1
                q.append([rr,cc,d+1])

for i in range(N):
    for j in range(M):
        if tomato[i][j]==1:
            q.append([i,j,0])
try:
    bfs(q[0][0],q[0][1])
except:
    print(-1)
    exit(0)

maxd=0
for i in range(N):
    for j in range(M):
        if 9999999>distances[i][j]>maxd:
            maxd=distances[i][j]
        if distances[i][j]==9999999 and tomato[i][j]==0:
            print(-1)
            exit(0)
print(maxd)