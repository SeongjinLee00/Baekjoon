from collections import deque

F,S,G,U,D=map(int,input().split())
visited=[0]*(F+1)

q=deque([[S,0]])
visited[S]=1

while q:
    now,d=q.popleft()
    if now==G:
        print(d)
        exit(0)
    
    if 1<=now+U<F+1 and not visited[now+U]:
        q.append([now+U,d+1])
        visited[now+U]=1
    if 1<=now-D<F+1 and not visited[now-D]:
        q.append([now-D,d+1])
        visited[now-D]=1

print('use the stairs')