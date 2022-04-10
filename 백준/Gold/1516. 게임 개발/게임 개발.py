from collections import deque

N=int(input())

graph=[[] for _ in range(N+1)]
prerequisites=[[] for _ in range(N+1)]
indegree=[0]*(N+1)
time=[0]*(N+1)
ans=[0]*(N+1)

for i in range(1,N+1):
    numbers=list(map(int,input().split()))
    time[i]=numbers[0]

    j=1
    while numbers[j]!=-1:
        graph[numbers[j]].append(i)
        prerequisites[i].append(numbers[j])
        indegree[i]+=1
        j+=1

q=deque()
for i in range(1,N+1):
    if indegree[i]==0:
        q.append([i,time[i]])

while q:
    n,t=q.popleft()
    ans[n]=t
    for v in graph[n]:
        indegree[v]-=1
        if indegree[v]==0:
            tmpmax=0
            for w in prerequisites[v]:
                if ans[w]>tmpmax:
                    tmpmax=ans[w]
            q.append([v,tmpmax+time[v]])

for i in range(1,N+1):
    print(ans[i])