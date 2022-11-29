from collections import deque

def solution(n, roads, sources, destination):
    graph=[[] for _ in range(n+1)]
    distances=[float('inf')]*(n+1)
    
    for a,b in roads:
        graph[a].append(b)
        graph[b].append(a)
    
    q=deque([[destination,0]])
    distances[destination]=0
        
    while q:
        now,d=q.popleft()
        
        for next in graph[now]:
            if distances[next]==float('inf'):
                q.append([next,d+1])
                distances[next]=d+1
    
    ret=[]
    
    for source in sources:
        if distances[source]==float('inf'):
            ret.append(-1)
        else:
            ret.append(distances[source])
    
    return ret