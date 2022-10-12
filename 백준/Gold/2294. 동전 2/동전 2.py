from collections import deque

N,K=map(int,input().split())

coins=[]
visited=[0]*(K+1)

for _ in range(N):
    coins.append(int(input()))

coins.sort()

if coins[0]>K:
    print(-1)
    exit(0)

q=deque()
for coin in coins:
    if coin>K:
        break
    q.append([coin,1])
    visited[coin]=1
while q:
    now,d = q.popleft()

    for coin in coins:
        if now+coin<=K and not visited[now+coin]:
            visited[now+coin]=d+1
            q.append([now+coin,d+1])

if visited[K]:
    print(visited[K])
else:
    print(-1)