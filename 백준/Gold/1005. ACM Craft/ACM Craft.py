from collections import deque
import sys
input=sys.stdin.readline

T=int(input())

for _ in range(T):
    N,K=map(int,input().split())
    times=[0]+list(map(int,input().split()))

    indegree=[0]*(N+1)
    graph=[[] for _ in range(N+1)]
    prerequisites=[[] for _ in range(N+1)]

    for _ in range(K):
        a,b=map(int,input().split())
        graph[a].append(b)
        indegree[b]+=1
        prerequisites[b].append(a)
    
    q=deque()

    for i in range(1,N+1):
        if indegree[i]==0:
            q.append([i,times[i]])

    ans=[0]*(N+1)
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
                q.append([v,tmpmax+times[v]])

    print(ans[int(input())])