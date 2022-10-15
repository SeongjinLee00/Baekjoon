from collections import deque
t=0
while True:
 
    n=int(input())
    t+=1

    if n==0:
        exit(0)
    a=[]
    for i in range(n):
        a.append(list(map(int,input().split())))
 
    visited=[]
    for i in range(n):
        visited.append([999999 for i in range(n)])
 
 
    dx=[0,0,-1,1]
    dy=[1,-1,0,0]
    def bfs(x,y):
        queue=deque()
        queue.append([x,y])
 
        visited[x][y]=a[x][y]
 
        while queue:
            x,y = queue.popleft()
 
            for i in range(4):
                nx=x+dx[i]
                ny=y+dy[i]
 
                # if x==n-1 and y==n-1:
                #     return visited[x][y]
 
                if nx<0 or nx >=n or ny<0 or ny>=n:
                    continue
 
                if visited[nx][ny]> visited[x][y]+a[nx][ny]:
                    visited[nx][ny]=visited[x][y]+a[nx][ny]
                    queue.append([nx,ny])
 
    bfs(0,0)
    print(f'Problem {t}: {visited[n-1][n-1]}')