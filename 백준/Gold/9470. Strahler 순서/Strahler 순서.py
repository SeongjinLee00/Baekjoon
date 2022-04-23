from collections import deque
import sys
input=sys.stdin.readline

T=int(input())

for t in range(1,T+1):
    K,M,P=map(int,input().split())

    indegree=[0]*(M+1)
    strahler=[0]*(M+1)
    graph=[[] for _ in range(M+1)]
    before=[[] for _ in range(M+1)]

    for _ in range(P):
        a,b=map(int,input().split())
        graph[a].append(b)
        before[b].append(a)
        indegree[b]+=1

    q=deque()

    for i in range(1,M+1):
        if indegree[i]==0:
            q.append(i)
            strahler[i]=1
    
    while q:

        now=q.popleft()

        for i in graph[now]:
            indegree[i]-=1
            if indegree[i]==0:
                tmp=[]
                for v in before[i]:
                    tmp.append(strahler[v])
                q.append(i)
                if tmp.count(max(tmp))>=2:
                    strahler[i]=max(tmp)+1
                else:
                    strahler[i]=max(tmp)

    print(t,max(strahler))