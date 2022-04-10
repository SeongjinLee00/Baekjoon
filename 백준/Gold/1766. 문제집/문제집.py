from heapq import heappush, heappop

V,E=map(int,input().split())

indegree=[0]*(V+1)

graph=[[] for _ in range(V+1)]

for _ in range(E):
    a,b=map(int,input().split())
    graph[a].append(b)

    indegree[b]+=1

def topological_sort():
    result=[]
    q=[]

    for i in range(1,V+1):
        if indegree[i]==0:
            heappush(q,i)
    while q:
        
        now=heappop(q)
        result.append(now)
        
        for i in graph[now]:
            indegree[i]-=1
            if indegree[i]==0:
                heappush(q,i)
    print(*result)

topological_sort()