from collections import deque

N,M=map(int,input().split())

graph=[[] for _ in range(N+1)]

indegree=[0]*(N+1)
answer={}

for _ in range(M):
    a,b=map(int,input().split())
    graph[a].append(b)
    indegree[b]+=1

q=deque()

for i in range(1,N+1):
    if indegree[i]==0:
        q.append([i,1])

while q:
    subject,semester=q.popleft()
    answer[subject]=semester

    for i in graph[subject]:
        indegree[i]-=1
        if indegree[i]==0:
            q.append([i,semester+1])

for i in range(1,N+1):
    print(answer[i],end=' ')