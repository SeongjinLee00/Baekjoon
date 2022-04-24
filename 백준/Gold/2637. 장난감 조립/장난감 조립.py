from collections import deque

N=int(input())
M=int(input())

indegree=[0]*(N+1)

needs=[[0]*(N+1) for _ in range(N+1)]

graph=[[] for _ in range(N+1)]

for _ in range(M):
    a,b,c=map(int,input().split())

    graph[b].append([a,c])
    indegree[a]+=1

basic=[]
q=deque()
for i in range(1,N+1):
    if indegree[i]==0:
        basic.append(i)
        q.append(i)

while q:
    now=q.popleft()

    for next,now_need in graph[now]:
        if now in basic:
            needs[next][now]+=now_need
        else:
            for i in range(1,N+1):
                needs[next][i]+=needs[now][i]*now_need
        
        indegree[next]-=1
        if indegree[next]==0:
            q.append(next)

for idx,val in enumerate(needs[N]):
    if idx in basic:
        print(idx,val)