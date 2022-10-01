from heapq import heappop, heappush

def solution(N, road, K):
    distances=[float('inf')]*N
    
    graph=[[] for _ in range(N)]
    
    for s,e,c in road:
        graph[s-1].append([c,e-1])
        graph[e-1].append([c,s-1])
    
    q=[[0,0]]
    distances[0]=0
    while q:
        travel,now=heappop(q)
        
        if travel>distances[now]:
            continue
            
        for distance,next in graph[now]:
            if distance+travel<distances[next]:
                distances[next]=distance+travel
                heappush(q,[distance+travel,next])

    ans=0
    for i in distances:
        if i<=K:
            ans+=1
    return ans