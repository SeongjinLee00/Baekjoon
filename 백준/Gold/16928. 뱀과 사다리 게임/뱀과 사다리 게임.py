from collections import deque

N,M=map(int,input().split())

visited=[100]*101
graph=[[] for _ in range(101)]
ladders=[[] for _ in range(101)]
snakes=[[] for _ in range(101)]

for i in range(1,100):
    graph[i].append(i+1)
    graph[i].append(i+2)
    graph[i].append(i+3)
    graph[i].append(i+4)
    graph[i].append(i+5)
    graph[i].append(i+6)

for _ in range(N):
    s,e=map(int,input().split())
    ladders[s].append(e)
for _ in range(M):
    s,e=map(int,input().split())
    snakes[s].append(e)

q=deque([[1,0]])

while q:
    n,d=q.popleft()
    if n==100:
        print(d)
        exit(0)
    
    if snakes[n]:
        q.appendleft([snakes[n][0],d])

    elif ladders[n]:
        q.appendleft([ladders[n][0],d])

    else:
        for next in graph[n]:
            if next<=100 and visited[next]>=d+1:
                q.append([next,d+1])
                visited[next]=d+1