from collections import deque
import sys
input=sys.stdin.readline

N=int(input())

time=[0]*(N+1)
indegree=[0]*(N+1)
graph=[[] for _ in range(N+1)]
prerequisites=[[] for _ in range(N+1)]
ans=[0]*(N+1)

for i in range(1,N+1):
    t,zzz,*w=map(int,input().split())
    time[i]=t

    for work in w:
        graph[work].append(i)
        indegree[i]+=1
    prerequisites[i]=w

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

print(max(ans))