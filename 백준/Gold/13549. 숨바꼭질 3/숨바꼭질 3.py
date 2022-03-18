from collections import deque

N,K=map(int,input().split())
flag=False
if N==0:
    N=1
    flag=True

visited=[]
def bfs(n):
    global visited
    q=deque([[n,0]])
    visited=[0]*100001
    visited[n]=-1
    while q:
        x,move=q.popleft()
        for i in range(3):
            if i==0:
                xx=x+1
                if 0<=xx<=100000 and not visited[xx]:
                    visited[xx]=move+1
                    q.append([xx,move+1])
                elif 0<=xx<=100000 and visited[xx]:
                    if move+1<visited[xx]:
                        visited[xx]=move+1
                        q.append([xx,move+1])
            elif i==1:
                xx=x-1
                if 0<=xx<=100000 and not visited[xx]:
                    visited[xx]=move+1
                    q.append([xx,move+1])
                elif 0<=xx<=100000 and visited[xx]:
                    if move+1<visited[xx]:
                        visited[xx]=move+1
                        q.append([xx,move+1])
            else:
                xx=2*x
                if 0<=xx<=100000 and not visited[xx]:
                    if move==0:
                        visited[xx]=-1
                    else:
                        visited[xx]=move
                    q.append([xx,move])
                elif 0<=xx<=100000 and visited[xx]:
                    if move==0:
                        visited[xx]=-1
                        q.append([xx,move])
                    if move<visited[xx]:
                        visited[xx]=move
                        q.append([xx,move])

bfs(N)
ans=visited[K]

if flag:
    if ans==-1:
        print(1)
    else:
        print(ans+1)
else:
    if ans==-1:
        print(0)
    else:
        print(ans)
