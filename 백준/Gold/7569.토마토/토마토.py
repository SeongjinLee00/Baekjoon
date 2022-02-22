from collections import deque

M,N,H=map(int,input().split()) # 가로로 M 세로로 N
tomato=[[] for _ in range(H)]

for h in range(H):
    for _ in range(N):
        tomato[h].append(list(map(int,input().split())))

distances=[[[9999999]*M for _ in range(N)] for _ in range(H)]

dr=[1,-1,0,0,0,0]
dc=[0,0,1,-1,0,0]
dh=[0,0,0,0,1,-1]
q=deque()
visited=[[[0]*M for _ in range(N)] for _ in range(H)]
def bfs(h,r,c):
    while q:
        h,r,c,d=q.popleft()
        visited[h][r][c]=1
        if d<distances[h][r][c]:
            distances[h][r][c]=d
        for i in range(6):
            rr=r+dr[i]
            cc=c+dc[i]
            hh=h+dh[i]
            if 0<=rr<N and 0<=cc<M and 0<=hh<H and not visited[hh][rr][cc] and tomato[hh][rr][cc]==0:
                visited[hh][rr][cc]=1
                q.append([hh,rr,cc,d+1])

for k in range(H):
    for i in range(N):
        for j in range(M):
            if tomato[k][i][j]==1:
                q.append([k,i,j,0])
try:
    bfs(q[0][0],q[0][1],q[0][2])
except:
    print(-1)
    exit(0)

maxd=0
for k in range(H):
    for i in range(N):
        for j in range(M):
            if 9999999>distances[k][i][j]>maxd:
                maxd=distances[k][i][j]
            if distances[k][i][j]==9999999 and tomato[k][i][j]==0:
                print(-1)
                exit(0)
print(maxd)