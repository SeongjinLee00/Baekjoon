from collections import deque

N,M=map(int,input().split())

graph=[[] for _ in range(N+1)]
indegree=[0]*(N+1)
for _ in range(M):
    num,*arr=map(int,input().split())

    for i in range(len(arr)-1):
        graph[arr[i]].append(arr[i+1])
        indegree[arr[i+1]]+=1

q=deque()
result=[]

for i in range(1,N+1):
    if indegree[i]==0:
        q.append(i)

while q:

    now=q.popleft()
    result.append(now)

    for i in graph[now]:
        indegree[i]-=1
        if indegree[i]==0:
            q.append(i)

if len(result)<N:
    print(0)
    exit(0)

for r in result:
    print(r)