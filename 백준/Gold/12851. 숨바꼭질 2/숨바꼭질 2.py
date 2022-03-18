from collections import deque

N,K=map(int,input().split())
ans=[]
def bfs(n):
    q=deque([[n,0]])
    visited=[0]*100001
    visited[n]=[1,0]
    while q:

        x,move=q.popleft()
        if x==K:
            ans.append(move)
        for i in range(3):
            if i==0:
                xx=x+1
            elif i==1:
                xx=x-1
            else:
                xx=2*x

            if 0<=xx<=100000 and not visited[xx]:
                visited[xx]=[1,move+1]
                q.append([xx,move+1])
            elif 0<=xx<=100000 and visited[xx]:
                if visited[xx][1]==move+1:
                    q.append([xx,move+1])

bfs(N)
print(ans[0])
print(len(ans))
