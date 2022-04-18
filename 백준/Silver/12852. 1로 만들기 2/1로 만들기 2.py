from collections import deque

N=int(input())

visited=[0]*1000001

q=deque([[N,[N]]])
visited[N]=1

while q:
    n,hist=q.popleft()
    if n==1:
        print(len(hist)-1)
        print(*hist)
        exit(0)
    for i in range(3):
        if i==0:
            if n%3==0:
                if not visited[n//3]:
                    visited[n//3]=1
                    q.append([n//3,hist+[n//3]])
        elif i==1:
            if n%2==0:
                if not visited[n//2]:
                    visited[n//2]=1
                    q.append([n//2,hist+[n//2]])
        elif i==2:
            if not visited[n-1]:
                visited[n-1]=1
                q.append([n-1,hist+[n-1]])