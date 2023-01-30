from collections import deque

a,b=map(int,input().split())

q=deque([[a,0]])

while q:
    now,d=q.popleft()
    if now==b:
        print(d+1)
        exit(0)
    if now>b:
        continue
    q.append([now*2,d+1])
    q.append([now*10+1,d+1])

print(-1)