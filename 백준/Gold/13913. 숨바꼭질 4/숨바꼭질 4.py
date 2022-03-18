from collections import deque

N,K=map(int,input().split())
visited=[]

if N>K:
    print(N-K)
    arr=[N-i for i in range(N-K+1)]
    print(*arr)
    exit(0)

def bfs(n):
    global visited
    q=deque([[[n],0]])
    visited=[[] for _ in range(100001)]
    visited[n]=1
    while q:
        path,move=q.popleft()
        if path[-1]==K:
            return move,path
        for i in range(3):
            if i==0:
                xx=path[-1]+1
            elif i==1:
                xx=path[-1]-1
            else:
                xx=2*path[-1]
            if 0<=xx<=100000 and not visited[xx]:
                visited[xx]=1
                q.append([path+[xx],move+1])

m,p=bfs(N)
print(m)
print(*p)